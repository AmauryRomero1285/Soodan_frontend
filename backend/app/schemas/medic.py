from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from app.schemas.profile import ProfileRead


class MedicBase(BaseModel):
    specialty: str
    license_number: str
    consultation_price: Decimal
    availability_price: Optional[Decimal] = None
    bio: Optional[str] = None
    doctor_value: Optional[float] = Field(5.0, ge=0, le=5)


class MedicCreate(MedicBase):
    hospital_id: Optional[int] = None


class MedicRead(MedicBase):
    id: int
    profiles_id: int
    profile: ProfileRead   # Información completa del perfil

    class Config:
        from_attributes = True


class MedicUpdate(BaseModel):
    specialty: Optional[str] = None
    consultation_price: Optional[Decimal] = None
    availability_price: Optional[Decimal] = None
    bio: Optional[str] = None
    hospital_id: Optional[int] = None