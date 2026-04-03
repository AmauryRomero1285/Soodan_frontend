from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .base import Base
import enum

class Role(str, enum.Enum):
    admin = "admin"
    medic = "medic"
    patient = "patient"

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)   # corresponde a "lastname" en tu SQL
    avatar_url = Column(String(255))
    phone_number = Column(String(20))
    role = Column(Enum(Role), default=Role.patient, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relaciones one-to-one
    medic = relationship("Medic", back_populates="profile", uselist=False, cascade="all, delete")
    patient = relationship("Patient", back_populates="profile", uselist=False, cascade="all, delete")

    # Para login y sesión
    password = Column(String(255), nullable=True)   # hashed
    is_verified = Column(Integer, default=0)        # 0 = no verificado, 1 = verificado