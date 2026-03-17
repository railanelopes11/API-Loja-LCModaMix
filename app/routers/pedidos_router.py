from fastapi import  APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal   
from app.models.pedido import Pedido
from app.models.item_pedido import ItemPedido
from app.schemas.pedido_schema import PedidoCreate, PedidoResponse, PedidoUpdateStatus
from app.schemas.item_pedido_schema import ItemPedidoCreate, ItemPedidoResponse

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
    db.commit()
    db.refresh(novo_pedido)

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

@router.post("/{pedido_id}/itens", response_model=ItemPedidoResponse)
def adicionar_item(pedido_id: int, item: ItemPedidoCreate, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    novo_item = ItemPedido(
        pedido_id=pedido_id,
        produto_id=item.produto_id,
        quantidade=item.quantidade
    )

    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)

    return novo_item

@router.get("/", response_model=List[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).all()

@router.get("/{pedido_id}", response_model=PedidoResponse)
def buscar_pedido(pedido_id: int, db: Session = Depends(get_db)):   
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.put("/{pedido_id}/status", response_model=PedidoResponse)
def atualizar_status_pedido(pedido_id: int, status_update: PedidoUpdateStatus, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    pedido.status = status_update.status
    db.commit()
    db.refresh(pedido)
    return pedido

@router.delete("/{pedido_id}")
def cancelar_pedido(pedido_id: int, db: Session = Depends(get_db)): 
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    db.delete(pedido)
    db.commit()
    return {"detail": "Pedido cancelado com sucesso"}   