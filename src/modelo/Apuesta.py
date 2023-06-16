from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from .declarative_base import Base



class Apuesta(Base):

    __tablename__ = 'Apuesta'
    id = Column(Integer,primary_key=True)
    valor = Column(Float())
    id_carrera = Column(Integer, ForeignKey('Carrera.id'))
    id_competidor = Column(Integer, ForeignKey('Competidor.id'))
    id_apostador = Column(Integer, ForeignKey('Apostador.id'))
    
    apostador = relationship('Apostador')
    carrera = relationship('Carrera')
    competidor = relationship('Competidor')