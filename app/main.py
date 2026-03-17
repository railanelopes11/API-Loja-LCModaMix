from fastapi import FastAPI
from app.routers import cliente_router, produto_router, pedidos_router
from app.database import Base, engine
import app.models


app = FastAPI(title="API Loja LC ModaMix", description="API para gerenciamento de clientes, produtos e pedidos da loja LC Moda Mix", version="1.0.0")
Base.metadata.create_all(bind=engine)



app.include_router(cliente_router.router)
app.include_router(produto_router.router) 
app.include_router(pedidos_router.router)

@app.get("/")
def root():
    return {"message": "API LC ModaMix funcionando"}
