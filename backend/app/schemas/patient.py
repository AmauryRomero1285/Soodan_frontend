# app/schemas/patient.py
from app.schemas.profile import ProfileRead
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from decimal import Decimal


class PatientBase(BaseModel):
    birth_date: Optional[date] = None
    blood_type: Optional[str] = Field(None, max_length=5)
    allergies: Optional[str] = None
    height: Optional[Decimal] = Field(None, gt=0, lt=300)
    weight: Optional[Decimal] = Field(None, gt=0, lt=700)


class PatientCreate(PatientBase):
    pass


class PatientRead(PatientBase):
    id: int
    profiles_id: int
    # Forward Reference
    profile: Optional["ProfileRead"] = None

    class Config:
        from_attributes = True


class PatientUpdate(BaseModel):
    birth_date: Optional[date] = None
    blood_type: Optional[str] = Field(None, max_length=5)
    allergies: Optional[str] = None
    height: Optional[Decimal] = Field(None, gt=0, lt=300)
    weight: Optional[Decimal] = Field(None, gt=0, lt=700)