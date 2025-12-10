from fastapi import FastAPI
from .database import Base, engine

# Aqui no futuro entraremos com os models antes desse create_all
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Controle de Ferramental – Kits")

@app.get("/")
def read_root():
    return {"status": "ok", "mensagem": "API Controle de Ferramental rodando"}
