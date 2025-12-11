from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ---------- ITENS ----------

class ItemBase(BaseModel):
    patrimonio: str
    descricao: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


# ---------- CHECKLIST SEMANAL ----------

class ChecklistSemanalBase(BaseModel):
    kit_id: int
    encarregado_id: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    patrimonios_declarados: Optional[str] = None  # texto com os patrimônios


class ChecklistSemanalCreate(ChecklistSemanalBase):
    pass


class ChecklistSemanal(ChecklistSemanalBase):
    id: int
    data_hora: datetime

    class Config:
        orm_mode = True
