from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey
from .base import Base

class Medic(Base):
    __tablename__ = "medics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    specialty = Column(String(100), nullable=False)
    license_number = Column(String(50), unique=True, nullable=False)
    doctor_value = Column(Numeric(2,1), default=5.0)
    bio = Column(Text)
    consultation_price = Column(Numeric(10,2), nullable=False)
    availability_price = Column(Numeric(10,2))
    hospital_id = Column(Integer, ForeignKey("hospital.id", ondelete="SET NULL"), nullable=True)

    profiles_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False, unique=True)
    profile = relationship("Profile", back_populates="medic")