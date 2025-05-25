from sqlalchemy.orm import Session
import models, schemas

from pydantic import BaseModel
from typing import Optional

class BolsaBase(BaseModel):
    nome: str
    valor: float
    descricao: Optional[str] = None

class BolsaCreate(BolsaBase):
    pass

def create_bolsa(db: Session, bolsa: schemas.BolsaCreate):
    db_bolsa = models.Bolsa(**bolsa.model_dump())
    db.add(db_bolsa)
    db.commit()
    db.refresh(db_bolsa)
    return db_bolsa

def get_bolsa(db: Session, bolsa_id: int):
    return db.query(models.Bolsa).filter(models.Bolsa.id == bolsa_id).first()

def get_bolsas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Bolsa).offset(skip).limit(limit).all()

def update_bolsa(db: Session, bolsa_id: int, bolsa: schemas.BolsaCreate):
    db_bolsa = db.query(models.Bolsa).filter(models.Bolsa.id == bolsa_id).first()
    if db_bolsa:
        for key, value in bolsa.model_dump().items():
            setattr(db_bolsa, key, value)
        db.commit()
        db.refresh(db_bolsa)
    return db_bolsa

def delete_bolsa(db: Session, bolsa_id: int):
    db_bolsa = db.query(models.Bolsa).filter(models.Bolsa.id == bolsa_id).first()
    if db_bolsa:
        db.delete(db_bolsa)
        db.commit()
        return True
    return False

def create_candidato(db: Session, candidato: schemas.CandidatoCreate):
    db_candidato = models.Candidato(**candidato.model_dump())
    db.add(db_candidato)
    db.commit()
    db.refresh(db_candidato)
    return db_candidato

def get_candidato(db: Session, candidato_id: int):
    return db.query(models.Candidato).filter(models.Candidato.id == candidato_id).first()

def get_candidatos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Candidato).offset(skip).limit(limit).all()

def update_candidato(db: Session, candidato_id: int, candidato: schemas.CandidatoCreate):
    db_candidato = db.query(models.Candidato).filter(models.Candidato.id == candidato_id).first()
    if db_candidato:
        for key, value in candidato.model_dump().items():
            setattr(db_candidato, key, value)
        db.commit()
        db.refresh(db_candidato)
    return db_candidato

def delete_candidato(db: Session, candidato_id: int):
    db_candidato = db.query(models.Candidato).filter(models.Candidato.id == candidato_id).first()
    if db_candidato:
        db.delete(db_candidato)
        db.commit()
        return True
    return False
