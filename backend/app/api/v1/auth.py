# app/api/v1/auth.py

from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import random

# Imports correctos:
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.dependencies import get_db, get_current_user, oauth2_scheme 

from app.models.profile import Profile
from app.models.medic import Medic
from app.models.patient import Patient
from app.models.session import UserSession
from app.email.service import send_email_background

from app.schemas.auth import (
    RegisterMedic,
    RegisterPatient,
    ForgotPassword,
    ResetPassword,
    VerifyCodeRequest
)

router = APIRouter(prefix="/auth", tags=["auth"])

# Almacenamiento temporal (→ Redis en producción)
verification_codes = {}  # {email: code}


@router.post("/register/medic", status_code=status.HTTP_201_CREATED)
def register_medic(
    data: RegisterMedic,
    background_tasks: BackgroundTasks,   # ← Corregido: plural
    db: Session = Depends(get_db)
):
    if db.query(Profile).filter(Profile.email == data.email).first():
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    new_profile = Profile(
        email=data.email,
        name=data.name,
        lastname=data.lastname,
        phone_number=data.phone_number,
        role="medic",
        password=get_password_hash(data.password),
        is_verified=0
    )
    db.add(new_profile)
    db.flush()

    hospital_id = data.hospital_id if hasattr(data, 'hospital_id') and data.hospital_id != 0 else None

    new_medic = Medic(
        profiles_id=new_profile.id,
        specialty=data.specialty,
        license_number=data.license_number,
        consultation_price=data.consultation_price,
        availability_price=data.availability_price,
        bio=data.bio,
        hospital_id=hospital_id,
    )
    db.add(new_medic)

    code = str(random.randint(100000, 999999))
    verification_codes[data.email] = code

    send_email_background(
        background_tasks=background_tasks,
        to_email=data.email,
        subject="Verifica tu cuenta en Soodan",
        template_name="verification.html",
        context={"code": code, "name": data.name}
    )

    db.commit()
    return {"message": "Médico registrado correctamente. Revisa tu correo para verificar la cuenta."}


@router.post("/register/patient", status_code=status.HTTP_201_CREATED)
def register_patient(
    data: RegisterPatient,
    background_tasks: BackgroundTasks,   # ← Corregido
    db: Session = Depends(get_db)
):
    # ... (mismo patrón que register_medic)
    # Copia el código de arriba y cambia solo lo necesario (role="patient" y Patient)
    if db.query(Profile).filter(Profile.email == data.email).first():
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    new_profile = Profile(
        email=data.email,
        name=data.name,
        lastname=data.lastname,
        phone_number=data.phone_number,
        role="patient",
        password=get_password_hash(data.password),
        is_verified=0
    )
    db.add(new_profile)
    db.flush()

    new_patient = Patient(
        profiles_id=new_profile.id,
        birth_date=data.birth_date,
        blood_type=data.blood_type,
        allergies=data.allergies,
        height=data.height,
        weight=data.weight,
    )
    db.add(new_patient)

    code = str(random.randint(100000, 999999))
    verification_codes[data.email] = code

    send_email_background(
        background_tasks=background_tasks,
        to_email=data.email,
        subject="Verifica tu cuenta en Soodan",
        template_name="verification.html",
        context={"code": code, "name": data.name}
    )

    db.commit()
    return {"message": "Paciente registrado correctamente. Revisa tu correo para verificar la cuenta."}


# ==================== NUEVO: Reenvío de código ====================
@router.post("/resend-verification")
def resend_verification(email: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user = db.query(Profile).filter(Profile.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if user.is_verified:
        raise HTTPException(status_code=400, detail="La cuenta ya está verificada")

    code = str(random.randint(100000, 999999))
    verification_codes[email] = code

    send_email_background(
        background_tasks=background_tasks,
        to_email=email,
        subject="Reenvío de código de verificación - Soodan",
        template_name="verification.html",
        context={"code": code, "name": user.name}
    )

    return {"message": "Código de verificación reenviado a tu correo"}


@router.post("/verify-code")
def verify_code(request: VerifyCodeRequest, db: Session = Depends(get_db)):
    stored_code = verification_codes.get(request.email)
    if not stored_code or stored_code != request.code:
        raise HTTPException(status_code=400, detail="Código inválido o expirado")

    user = db.query(Profile).filter(Profile.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user.is_verified = 1
    db.commit()
    verification_codes.pop(request.email, None)

    return {"message": "Cuenta verificada correctamente"}



@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    # form_data.username = email
    user = db.query(Profile).filter(Profile.email == form_data.username).first()

    if not user or not user.password or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_verified:
        raise HTTPException(
            status_code=403,
            detail="Debes verificar tu cuenta primero"
        )

    # Expiración según rol
    expires = timedelta(days=30) if user.role == "patient" else timedelta(hours=24)

    token = create_access_token(
        subject={"sub": user.id, "role": user.role},   # role como string
        expires_delta=expires
    )

    # Sesión persistente
    session = db.query(UserSession).filter(UserSession.user_id == user.id).first()
    if session:
        session.token = token
        session.is_active = True
    else:
        db.add(UserSession(user_id=user.id, token=token))

    db.commit()

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "lastname": user.lastname,
            "role": user.role
        }
    }

@router.post("/logout")
def logout(
    current_user: Profile = Depends(get_current_user),
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    """Logout seguro con invalidación de sesión persistente"""
    
    try:
        # Buscar y desactivar la sesión actual
        session = db.query(UserSession).filter(
            UserSession.user_id == current_user.id,
            UserSession.is_active == True
        ).first()

        if session:
            session.is_active = False
            # Opcional: puedes limpiar el token por seguridad
            # session.token = ""
            db.commit()

        return {
            "message": "Sesión cerrada correctamente",
            "user_id": current_user.id
        }

    except Exception as e:
        print(f"Error en logout: {e}")
        # Aún así devolvemos éxito por UX (no revelar errores internos)
        return {"message": "Sesión cerrada correctamente"}
@router.post("/logout/all")
def logout_all_sessions(
    current_user: Profile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Cierra todas las sesiones activas del usuario"""
    db.query(UserSession).filter(
        UserSession.user_id == current_user.id,
        UserSession.is_active == True
    ).update({"is_active": False})
    
    db.commit()
    
    return {"message": "Todas las sesiones han sido cerradas"}

@router.post("/forgot-password")
def forgot_password(
    data: ForgotPassword,
    background_tasks: BackgroundTasks,     # ← plural correcto
    db: Session = Depends(get_db)
):
    user = db.query(Profile).filter(Profile.email == data.email).first()
    if not user:
        # Por seguridad no revelamos si el email existe
        return {"message": "Si el email existe, recibirás un código de recuperación"}

    code = str(random.randint(100000, 999999))
    verification_codes[f"reset_{data.email}"] = code

    # Enviar email con la plantilla correcta
    send_email_background(
        background_tasks=background_tasks,
        to_email=data.email,
        subject="Recuperación de contraseña - Soodan",
        template_name="password_reset.html",      # ← .html incluido
        context={"code": code}
    )

    return {"message": "Código de recuperación enviado a tu email"}

@router.post("/reset-password")
def reset_password(data: ResetPassword, db: Session = Depends(get_db)):
    email = None
    for key, val in list(verification_codes.items()):
        if key.startswith("reset_") and val == data.token:
            email = key.replace("reset_", "")
            break

    if not email:
        raise HTTPException(status_code=400, detail="Código inválido o expirado")

    user = db.query(Profile).filter(Profile.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user.password = get_password_hash(data.new_password)
    db.commit()
    verification_codes.pop(f"reset_{email}", None)

    return {"message": "Contraseña actualizada correctamente"}