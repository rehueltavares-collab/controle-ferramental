from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from . import models, schemas

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Controle de Ferramental – Kits")


# ---------- DEPENDÊNCIA DE BANCO ----------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- ROTA DE SAÚDE ----------

@app.get("/")
def read_root():
    return {"status": "ok", "mensagem": "API Controle de Ferramental rodando"}


# ---------- ITENS ----------

@app.post("/itens/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(
        patrimonio=item.patrimonio,
        descricao=item.descricao,
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/itens/", response_model=List[schemas.Item])
def list_itens(db: Session = Depends(get_db)):
    return db.query(models.Item).all()


# ---------- CHECKLIST SEMANAL ----------

@app.post("/checklists-semanais/", response_model=schemas.ChecklistSemanal)
def create_checklist(payload: schemas.ChecklistSemanalCreate,
                     db: Session = Depends(get_db)):
    db_check = models.ChecklistSemanal(
        kit_id=payload.kit_id,
        encarregado_id=payload.encarregado_id,
        latitude=payload.latitude,
        longitude=payload.longitude,
        patrimonios_declarados=payload.patrimonios_declarados,
    )
    db.add(db_check)
    db.commit()
    db.refresh(db_check)
    return db_check


@app.get("/checklists-semanais/", response_model=List[schemas.ChecklistSemanal])
def list_checklists(db: Session = Depends(get_db)):
    return db.query(models.ChecklistSemanal).all()

