# app/schemas/medic.py
from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from app.schemas.profile import ProfileRead



class MedicBase(BaseModel):
    specialty: str = Field(..., min_length=3, max_length=100)
    license_number: str = Field(..., min_length=5, max_length=50)
    consultation_price: Decimal = Field(..., gt=0)
    availability_price: Optional[Decimal] = Field(None, gt=0)
    bio: Optional[str] = Field(None, max_length=1000)
    doctor_value: Optional[float] = Field(5.0, ge=0, le=5)


class MedicCreate(MedicBase):
    hospital_id: Optional[int] = None


class MedicRead(MedicBase):
    id: int
    profiles_id: int
    # Usamos Forward Reference para evitar ciclo
    profile: Optional["ProfileRead"] = None

    class Config:
        from_attributes = True


class MedicUpdate(BaseModel):
    specialty: Optional[str] = Field(None, min_length=3, max_length=100)
    consultation_price: Optional[Decimal] = Field(None, gt=0)
    availability_price: Optional[Decimal] = Field(None, gt=0)
    bio: Optional[str] = Field(None, max_length=1000)
    hospital_id: Optional[int] = None