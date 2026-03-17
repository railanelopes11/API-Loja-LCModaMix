from pydantic import BaseModel

class ItemPedidoBase(BaseModel):
    produto_id: int
    quantidade: int
    
    

class ItemPedidoCreate(ItemPedidoBase):
   pass

class ItemPedidoResponse(ItemPedidoBase):
    id: int
    pedido_id: int

    class Config:
        from_attributes = True