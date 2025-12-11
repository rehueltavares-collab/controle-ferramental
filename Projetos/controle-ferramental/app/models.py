from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Text
from datetime import datetime
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # ENCARGADO, COLABORADOR etc.

class Obra(Base):
    __tablename__ = "obras"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=True)

class Item(Base):
    __tablename__ = "itens"
    id = Column(Integer, primary_key=True, index=True)
    patrimonio = Column(String, unique=True, index=True, nullable=False)
    descricao = Column(String, nullable=True)
    status = Column(String, default="ATIVO")

class Kit(Base):
    __tablename__ = "kits"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

class KitItem(Base):
    __tablename__ = "kit_itens"
    id = Column(Integer, primary_key=True, index=True)
    kit_id = Column(Integer, ForeignKey("kits.id"))
    item_id = Column(Integer, ForeignKey("itens.id"))

class RetiradaKit(Base):
    __tablename__ = "retiradas_kit"
    id = Column(Integer, primary_key=True, index=True)
    kit_id = Column(Integer, ForeignKey("kits.id"))
    encarregado_id = Column(Integer, ForeignKey("usuarios.id"))
    obra_id = Column(Integer, ForeignKey("obras.id"))
    data_hora = Column(DateTime, default=datetime.utcnow)
    foto_inicial = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

class SubResponsabilidade(Base):
    __tablename__ = "sub_responsabilidades"
    id = Column(Integer, primary_key=True, index=True)
    retirada_id = Column(Integer, ForeignKey("retiradas_kit.id"))
    item_id = Column(Integer, ForeignKey("itens.id"))
    colaborador_nome = Column(String, nullable=False)
    data_hora_repassado = Column(DateTime, default=datetime.utcnow)
    data_hora_devolucao = Column(DateTime, nullable=True)

class ChecklistSemanal(Base):
    __tablename__ = "checklists_semanal"
    id = Column(Integer, primary_key=True, index=True)
    kit_id = Column(Integer, ForeignKey("kits.id"))
    encarregado_id = Column(Integer, ForeignKey("usuarios.id"))
    data_hora = Column(DateTime, default=datetime.utcnow)
    foto = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    patrimonios_declarados = Column(Text, nullable=True)
