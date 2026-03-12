from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.item_pedido import ItemPedido
from app.schemas.item_pedido_schema import ItemPedidoCreate, ItemPedidoResponse

router = APIRouter(prefix="/itens-pedido", tags=["ItensPedido"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ItemPedidoResponse)
def criar_item(item: ItemPedidoCreate, db: Session = Depends(get_db)):
    novo_item = ItemPedido(**item.model_dump())
    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)
    return novo_item

@router.get("/", response_model=List[ItemPedidoResponse])
def listar_itens(db: Session = Depends(get_db)):
    return db.query(ItemPedido).all()
