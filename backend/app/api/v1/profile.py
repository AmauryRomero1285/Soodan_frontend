# app/api/v1/profile.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_db, get_current_user
from app.models.profile import Profile
from app.models.medic import Medic
from app.models.patient import Patient

from app.schemas.profile import ProfileUpdate, ProfileRead

router = APIRouter(prefix="/me", tags=["profile"])


@router.get("/", response_model=ProfileRead)
def get_current_profile(current_user: Profile = Depends(get_current_user)):
    """Ya lo tenías como /api/v1/me"""
    return current_user


@router.patch("/", response_model=ProfileRead)
def update_current_profile(
    data: ProfileUpdate,
    current_user: Profile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Actualiza el perfil del usuario logueado"""
    # Actualizar campos comunes del Profile
    if data.name is not None:
        current_user.name = data.name
    if data.lastname is not None:
        current_user.lastname = data.lastname
    if data.phone_number is not None:
        current_user.phone_number = data.phone_number
    if data.avatar_url is not None:
        current_user.avatar_url = data.avatar_url

    # Actualizar campos específicos según rol
    if current_user.role == "medic" and current_user.medic:
        medic = current_user.medic
        if data.specialty is not None:
            medic.specialty = data.specialty
        if data.bio is not None:
            medic.bio = data.bio
        if data.consultation_price is not None:
            medic.consultation_price = data.consultation_price
        if data.availability_price is not None:
            medic.availability_price = data.availability_price
        if data.hospital_id is not None:
            medic.hospital_id = data.hospital_id

    elif current_user.role == "patient" and current_user.patient:
        patient = current_user.patient
        if data.birth_date is not None:
            patient.birth_date = data.birth_date
        if data.blood_type is not None:
            patient.blood_type = data.blood_type
        if data.allergies is not None:
            patient.allergies = data.allergies
        if data.height is not None:
            patient.height = data.height
        if data.weight is not None:
            patient.weight = data.weight

    db.commit()
    db.refresh(current_user)
    return current_user


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_current_profile(
    current_user: Profile = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """DELETE técnico: elimina el perfil + medic/patient (cascade)"""
    # Opcional: si quieres pedir confirmación, puedes agregar un parámetro
    db.delete(current_user)   # Gracias al CASCADE en la BD, borra Medic o Patient automáticamente
    db.commit()

    return None  # 204 No Content