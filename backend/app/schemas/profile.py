# app/schemas/profile.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime
from decimal import Decimal


class ProfileBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=100)
    lastname: str = Field(..., min_length=2, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=20)
    avatar_url: Optional[str] = None


class ProfileRead(ProfileBase):
    id: int
    role: str
    is_verified: bool = False
    created_at: datetime

    # Relaciones (Forward References)
    medic: Optional["MedicRead"] = None
    patient: Optional["PatientRead"] = None

    class Config:
        from_attributes = True


class ProfileUpdate(BaseModel):
    """Schema usado en PATCH /api/v1/me"""
    # Campos comunes
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    lastname: Optional[str] = Field(None, min_length=2, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=20)
    avatar_url: Optional[str] = None

    # Campos específicos de Médico
    specialty: Optional[str] = Field(None, min_length=3, max_length=100)
    bio: Optional[str] = Field(None, max_length=1000)
    consultation_price: Optional[Decimal] = Field(None, gt=0)
    availability_price: Optional[Decimal] = Field(None, gt=0)
    hospital_id: Optional[int] = None

    # Campos específicos de Paciente
    birth_date: Optional[date] = None
    blood_type: Optional[str] = Field(None, max_length=5)
    allergies: Optional[str] = None
    height: Optional[Decimal] = Field(None, gt=0, lt=300)
    weight: Optional[Decimal] = Field(None, gt=0, lt=700)

    class Config:
        from_attributes = True


class ChangePassword(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=8)


# ====================== RESOLVER REFERENCIAS CIRCULARES =====================
# Importamos al final para evitar ciclos
from .medic import MedicRead
from .patient import PatientRead

ProfileRead.model_rebuild()