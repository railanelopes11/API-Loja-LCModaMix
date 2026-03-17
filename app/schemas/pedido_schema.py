from datetime import datetime
from pydantic import BaseModel
from typing import List
from .item_pedido_schema import ItemPedidoCreate, ItemPedidoResponse

class PedidoBase(BaseModel):
    cliente_id: int
    status: str
    
class PedidoCreate(BaseModel):
    cliente_id: int
    itens : List[ItemPedidoCreate]
    status: str = "Pendente"

class PedidoUpdateStatus(BaseModel):
    status : str
   
class PedidoResponse(BaseModel):
    id: int
    cliente_id: int
    status: str
    data_pedido: datetime
    itens : List[ItemPedidoResponse]

    class Config:
        from_attributes = True

