from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean

from .declarative_base import Base



class Competidor(Base):

    __tablename__ = 'Competidor'
    id = Column(Integer,primary_key=True)
    nombre = Column(String(50))
    probabilidad = Column(Float())
    cuota = Column(Float())
    ganador = Column(Boolean)
    id_carrera = Column(Integer, ForeignKey('Carrera.id'))