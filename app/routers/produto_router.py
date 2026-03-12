from fastapi import  APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.produto import Produto  
from app.schemas.produto_schema import ProdutoCreate, ProdutoResponse, ProdutoUpdate

router = APIRouter(prefix="/produtos", tags=["Produtos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProdutoResponse)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = Produto(**produto.model_dump())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

@router.get("/", response_model=List[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto      

@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, produto_atualizado: ProdutoUpdate, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produto.nome = produto_atualizado.nome
    produto.descricao = produto_atualizado.descricao
    produto.preco = produto_atualizado.preco
    db.commit()
    db.refresh(produto)
    return produto

@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()
    return {"detail": "Produto deletado com sucesso"}

