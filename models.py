from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Bolsa(Base):
    __tablename__ = "bolsas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    valor = Column(Float)
    descricao = Column(String)
    candidatos = relationship("Candidato", back_populates="bolsa")

class Candidato(Base):
    __tablename__ = "candidatos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    bolsa_id = Column(Integer, ForeignKey("bolsas.id"))
    bolsa = relationship("Bolsa", back_populates="candidatos")