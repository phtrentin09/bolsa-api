# schemas.py
from pydantic import BaseModel
from typing import Optional


class BolsaBase(BaseModel):
    nome: str
    valor: float
    descricao: Optional[str] = None


class BolsaCreate(BolsaBase):
    pass


class Bolsa(BolsaBase):
    id: int

    class Config:
        orm_mode = True


class CandidatoBase(BaseModel):
    nome: str
    email: str


class CandidatoCreate(CandidatoBase):
    pass


class Candidato(CandidatoBase):
    id: int

    class Config:
        orm_mode = True
