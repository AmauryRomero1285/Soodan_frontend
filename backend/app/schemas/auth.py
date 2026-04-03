from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date

# ====================== REGISTRO ======================

class RegisterBase(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=100)
    lastname: str = Field(..., min_length=2, max_length=100)
    phone_number: Optional[str] = Field(None, max_length=20)
    password: str = Field(..., min_length=8, max_length=128)


class RegisterMedic(RegisterBase):
    specialty: str = Field(..., min_length=3, max_length=100)
    license_number: str = Field(..., min_length=5, max_length=50)
    consultation_price: float = Field(..., gt=0)
    availability_price: Optional[float] = Field(None, gt=0)
    bio: Optional[str] = Field(None, max_length=1000)
    hospital_id: Optional[int] = None


class RegisterPatient(RegisterBase):
    birth_date: Optional[date] = None
    blood_type: Optional[str] = Field(None, max_length=5)
    allergies: Optional[str] = None
    height: Optional[float] = Field(None, gt=0, lt=300)
    weight: Optional[float] = Field(None, gt=0, lt=700)


# ====================== LOGIN Y AUTH ======================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: dict


class TokenData(BaseModel):
    user_id: int
    role: str

class LogoutResponse(BaseModel):
    message: str

# ====================== RECUPERACIÓN DE CONTRASEÑA ======================

class ForgotPassword(BaseModel):
    email: EmailStr


class ResetPassword(BaseModel):
    token: str          # código de verificación o token JWT
    new_password: str = Field(..., min_length=8)


# ====================== VERIFICACIÓN ======================

class VerifyCodeRequest(BaseModel):
    email: EmailStr
    code: str = Field(..., min_length=6, max_length=6)