from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    data_pedido = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    status = Column(String, default="Pendente")

    cliente = relationship("Cliente", back_populates="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido")