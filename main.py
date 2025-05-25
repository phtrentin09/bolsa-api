from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud, database, auth

app = FastAPI(title="Bolsa de Estudos API", description="API para gerenciar bolsas e candidatos")

models.Base.metadata.create_all(bind=database.engine)

security = HTTPBasic()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/bolsas/", response_model=schemas.Bolsa)
def create_bolsa(bolsa: schemas.BolsaCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    auth.authenticate(credentials)
    return crud.create_bolsa(db=db, bolsa=bolsa)

@app.get("/bolsas/", response_model=List[schemas.Bolsa])
def read_bolsas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_bolsas(db, skip=skip, limit=limit)

@app.get("/bolsas/{bolsa_id}", response_model=schemas.Bolsa)
def read_bolsa(bolsa_id: int, db: Session = Depends(get_db)):
    db_bolsa = crud.get_bolsa(db, bolsa_id=bolsa_id)
    if db_bolsa is None:
        raise HTTPException(status_code=404, detail="Bolsa não encontrada")
    return db_bolsa

@app.put("/bolsas/{bolsa_id}", response_model=schemas.Bolsa)
def update_bolsa(bolsa_id: int, bolsa: schemas.BolsaCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    auth.authenticate(credentials)
    db_bolsa = crud.update_bolsa(db, bolsa_id=bolsa_id, bolsa=bolsa)
    if db_bolsa is None:
        raise HTTPException(status_code=404, detail="Bolsa não encontrada")
    return db_bolsa

@app.delete("/bolsas/{bolsa_id}")
def delete_bolsa(bolsa_id: int, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    auth.authenticate(credentials)
    if not crud.delete_bolsa(db, bolsa_id=bolsa_id):
        raise HTTPException(status_code=404, detail="Bolsa não encontrada")
    return {"detail": "Bolsa deletada"}

@app.post("/candidatos/", response_model=schemas.Candidato)
def create_candidato(candidato: schemas.CandidatoCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    auth.authenticate(credentials)
    return crud.create_candidato(db=db, candidato=candidato)

@app.get("/candidatos/", response_model=List[schemas.Candidato])
def read_candidatos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_candidatos(db, skip=skip, limit=limit)

@app.get("/candidatos/{candidato_id}", response_model=schemas.Candidato)
def read_candidato(candidato_id: int, db: Session = Depends(get_db)):
    db_candidato = crud.get_candidato(db, candidato_id=candidato_id)
    if db_candidato is None:
        raise HTTPException(status_code=404, detail="Candidato não encontrado")
    return db_candidato

@app.put("/candidatos/{candidato_id}", response_model=schemas.Candidato)
def update_candidato(candidato_id: int, candidato: schemas.CandidatoCreate, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    auth.authenticate(credentials)
    db_candidato = crud.update_candidato(db, candidato_id=candidato_id, candidato=candidato)
    if db_candidato is None:
        raise HTTPException(status_code=404, detail="Candidato não encontrado")
    return db_candidato

@app.delete("/candidatos/{candidato_id}")
def delete_candidato(candidato_id: int, db: Session = Depends(get_db), credentials: HTTPBasicCredentials = Depends(security)):
    auth.authenticate(credentials)
    if not crud.delete_candidato(db, candidato_id=candidato_id):
        raise HTTPException(status_code=404, detail="Candidato não encontrado")
    return {"detail": "Candidato deletado"}