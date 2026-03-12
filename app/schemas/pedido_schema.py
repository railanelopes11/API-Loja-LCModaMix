from datetime import datetime
from pydantic import BaseModel
from typing import List
from .item_pedido_schema import ItemPedidoCreate, ItemPedidoResponse

class PedidoBase(BaseModel):
    cliente_id: int
    status: str
    

class PedidoCreate(PedidoBase):
    itens : List[ItemPedidoCreate]

class PedidoResponse(PedidoBase):
    id: int
    data_pedido: datetime
    itens : List[ItemPedidoResponse]

    class Config:
        from_attributes = True

