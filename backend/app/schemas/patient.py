from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from decimal import Decimal
from app.schemas.profile import ProfileRead


class PatientBase(BaseModel):
    birth_date: Optional[date] = None
    blood_type: Optional[str] = Field(None, max_length=5)
    allergies: Optional[str] = None
    height: Optional[Decimal] = Field(None, gt=0)
    weight: Optional[Decimal] = Field(None, gt=0)


class PatientCreate(PatientBase):
    pass


class PatientRead(PatientBase):
    id: int
    profiles_id: int
    profile: ProfileRead

    class Config:
        from_attributes = True


class PatientUpdate(BaseModel):
    birth_date: Optional[date] = None
    blood_type: Optional[str] = None
    allergies: Optional[str] = None
    height: Optional[Decimal] = None
    weight: Optional[Decimal] = None