from sqlalchemy import Column, DateTime, Integer, String
from app.database import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True)
    telefone = Column(String)
    data_criacao = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    pedidos = relationship("Pedido", back_populates="cliente")

    

    