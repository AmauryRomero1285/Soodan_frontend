from sqlalchemy import Column, Integer, Date, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    birth_date = Column(Date)
    blood_type = Column(String(5))
    allergies = Column(Text)
    height = Column(Numeric(5,2))
    weight = Column(Numeric(5,2))

    profiles_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False, unique=True)
    profile = relationship("Profile", back_populates="patient")