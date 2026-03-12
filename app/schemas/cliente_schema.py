from datetime import datetime
from pydantic import BaseModel


class ClienteBase(BaseModel):
    nome: str
    email: str
    telefone: str
    

class ClienteCreate(ClienteBase):
    pass
    
class ClienteUpdate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    data_criacao: datetime
    
    class Config:
        from_attributes = True
