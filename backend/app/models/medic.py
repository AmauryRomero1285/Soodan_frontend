# app/models/medic.py
from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Medic(Base):
    __tablename__ = "medics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    specialty = Column(String(100), nullable=False)
    license_number = Column(String(50), unique=True, nullable=False)
    doctor_value = Column(Numeric(2,1), default=5.0)
    bio = Column(Text)
    consultation_price = Column(Numeric(10,2), nullable=False)
    availability_price = Column(Numeric(10,2))

    # Clave foránea hacia Hospital
    hospital_id = Column(Integer, ForeignKey("hospitals.id", ondelete="SET NULL"), nullable=True)
    
    # Clave foránea hacia Profile
    profiles_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False, unique=True)

    # Relaciones
    profile = relationship("Profile", back_populates="medic", uselist=False)
    hospital = relationship("Hospital", back_populates="medics", lazy="selectin")

    def __repr__(self):
        return f"<Medic {self.license_number} - {self.specialty}>"