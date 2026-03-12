from fastapi import  APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal   
from app.models.pedido import Pedido
from app.models.item_pedido import ItemPedido
from app.schemas.pedido_schema import PedidoCreate, PedidoResponse

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  

@router.post("/", response_model=PedidoResponse)
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):


    novo_pedido = Pedido(
        cliente_id=pedido.cliente_id,
        status=pedido.status if pedido.status else "Pendente"
    )

    db.add(novo_pedido)
    db.flush()

    for item in pedido.itens:
        item_pedido = ItemPedido(
            pedido_id=novo_pedido.id,
            produto_id=item.produto_id,
            quantidade=item.quantidade,
        )
        db.add(item_pedido)

        db.commit()
        db.refresh(novo_pedido)

        return novo_pedido





@router.get("/", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).all()