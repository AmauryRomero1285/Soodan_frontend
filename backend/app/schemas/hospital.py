# app/schemas/hospital.py
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .medic import MedicRead


class HospitalBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=150)
    address: Optional[str] = Field(None, max_length=255)
    phone: Optional[str] = Field(None, max_length=20)


class HospitalCreate(HospitalBase):
    pass


class HospitalRead(HospitalBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class HospitalUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = None


# Schema para mostrar hospital con sus médicos (opcional)
class HospitalWithMedics(HospitalRead):
    medics: List["MedicRead"] = []

    class Config:
        from_attributes = True
        

HospitalWithMedics.model_rebuild()