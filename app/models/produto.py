from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Integer)
    estoque = Column(Integer)

    itens_pedido = relationship("ItemPedido", back_populates="produto")