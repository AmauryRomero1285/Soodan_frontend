from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from app.schemas.auth import RegisterBase

class Role(str):
    admin = "admin"
    medic = "medic"
    patient = "patient"


class ProfileBase(BaseModel):
    email: EmailStr
    name: str
    lastname: str
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None


class ProfileCreate(RegisterBase):
    """Usado internamente para crear el perfil"""
    role: str


class ProfileRead(ProfileBase):
    id: int
    role: str
    created_at: datetime
    is_verified: bool = False

    class Config:
        from_attributes = True


class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None