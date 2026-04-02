# app/models/hospital.py
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.models.base import Base


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    address = Column(String(255))
    phone = Column(String(20))
    created_at = Column(DateTime, server_default=func.now())

    # Relación con médicos (un hospital puede tener muchos médicos)
    medics = relationship("Medic", back_populates="hospital", lazy="selectin")

    def __repr__(self):
        return f"<Hospital {self.name}>"