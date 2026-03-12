from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base       

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    quantidade = Column(Integer)
    

    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto", back_populates="itens_pedido")