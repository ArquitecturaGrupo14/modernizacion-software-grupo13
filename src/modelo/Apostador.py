from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .declarative_base import Base

# Crear tabla Apostador

class Apostador(Base):
    __tablename__ = 'Apostador'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
