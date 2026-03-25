from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.dependencies import get_db
from app.models.profile import Profile
from app.models.medic import Medic
from app.models.patient import Patient
from app.models.session import UserSession
from app.schemas.auth import (
    RegisterMedic, RegisterPatient, LoginRequest,
    ForgotPassword, ResetPassword
)
from datetime import timedelta
import random

router = APIRouter(prefix="/auth", tags=["auth"])

# Código de verificación simple (puedes guardar en Redis o tabla temporal en prod)
verification_codes = {}   # {email: code} → reemplazar por Redis en producción

@router.post("/register/medic", status_code=201)
def register_medic(data: RegisterMedic, db: Session = Depends(get_db)):
    if db.query(Profile).filter(Profile.email == data.email).first():
        raise HTTPException(400, "El email ya está registrado")

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

    new_medic = Medic(
        profiles_id=new_profile.id,
        specialty=data.specialty,
        license_number=data.license_number,
        consultation_price=data.consultation_price,
        # ...
    )
    db.add(new_medic)

    # Generar código de verificación
    code = str(random.randint(100000, 999999))
    verification_codes[data.email] = code

    # TODO: Enviar email con el código (usa smtplib o aiosmtplib + Jinja)

    db.commit()
    return {"message": "Médico registrado. Verifica tu email con el código enviado."}

@router.post("/register/patient", status_code=201)
def register_patient(data: RegisterPatient, db: Session = Depends(get_db)):
    # Similar al anterior, pero role="patient" y crea Patient
    ...

@router.post("/verify-code")
def verify_code(email: str, code: str, db: Session = Depends(get_db)):
    if verification_codes.get(email) != code:
        raise HTTPException(400, "Código inválido")
    
    user = db.query(Profile).filter(Profile.email == email).first()
    if user:
        user.is_verified = 1
        db.commit()
        del verification_codes[email]
        return {"message": "Cuenta verificada correctamente"}
    raise HTTPException(404, "Usuario no encontrado")

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(Profile).filter(Profile.email == data.email).first()
    
    if not user or not verify_password(data.password, user.password or ""):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Credenciales inválidas")

    if not user.is_verified:
        raise HTTPException(403, "Debes verificar tu cuenta primero")

    # Diferente expiración según rol
    expires = timedelta(days=30) if user.role == "patient" else timedelta(days=1)

    token = create_access_token(
        subject={"sub": user.id, "role": user.role.value},
        expires_delta=expires
    )

    # Sesión persistente (upsert)
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
            "role": user.role.value,
            "name": user.name,
            "email": user.email
        }
    }

@router.post("/forgot-password")
def forgot_password(data: ForgotPassword, db: Session = Depends(get_db)):
    user = db.query(Profile).filter(Profile.email == data.email).first()
    if not user:
        # No revelar si existe o no (seguridad)
        return {"message": "Si el email existe, recibirás un código de recuperación"}

    code = str(random.randint(100000, 999999))
    verification_codes[f"reset_{data.email}"] = code   # prefijo para distinguir

    # TODO: Enviar email con código de recuperación

    return {"message": "Código de recuperación enviado a tu email"}

@router.post("/reset-password")
def reset_password(data: ResetPassword, db: Session = Depends(get_db)):
    email = None
    for key, val in verification_codes.items():
        if key.startswith("reset_") and val == data.token:   # en prod usa JWT o token seguro
            email = key.replace("reset_", "")
            break

    if not email:
        raise HTTPException(400, "Token inválido o expirado")

    user = db.query(Profile).filter(Profile.email == email).first()
    if user:
        user.password = get_password_hash(data.new_password)
        db.commit()
        del verification_codes[f"reset_{email}"]
        return {"message": "Contraseña actualizada correctamente"}
    
    raise HTTPException(404, "Usuario no encontrado")