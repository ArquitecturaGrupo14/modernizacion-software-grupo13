from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .declarative_base import Base

# Crear tabla Carrera

class Carrera(Base):
    __tablename__ = 'Carrera'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    abierta = Column(Boolean)
    competidor = relationship('Competidor',cascade='all,delete,delete-orphan')