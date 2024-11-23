from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient, errors
from typing import List, Optional

# Inicializa o app FastAPI
app = FastAPI()

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Loja"]
colecao = db["produtos"]

# Configura o índice único no campo "codigo"
colecao.create_index("codigo", unique=True)

# Modelos de Dados
class Produto(BaseModel):
    codigo: int
    nome: str
    quantidade: int
    valor: float

class ProdutoUpdate(BaseModel):
    nome: Optional[str]
    quantidade: Optional[int]
    valor: Optional[float]

class ProdutoResponse(BaseModel):
    data: List[Produto]

# Rota GET - Listar todos os produtos
@app.get("/produtos", response_model=ProdutoResponse)
async def listar_produtos():
    produtos = list(colecao.find({}, {"_id": 0}))
    return {"data": produtos}

# Rota POST - Criar um novo produto
@app.post("/produtos", status_code=201)
async def criar_produto(produto: Produto):
    try:
        colecao.insert_one(produto.dict())
        return {"message": "Produto inserido com sucesso.", "produto": produto}
    except errors.DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Produto com este código já existe.")

# Rota PATCH - Atualizar um produto existente
@app.patch("/produtos/{codigo}", status_code=200)
async def atualizar_produto(codigo: int, produto_update: ProdutoUpdate):
    try:
        produto_existente = colecao.find_one({"codigo": codigo})
        if not produto_existente:
            raise HTTPException(status_code=404, detail="Produto não encontrado.")

        campos_para_atualizar = {k: v for k, v in produto_update.dict().items() if v is not None}

        if not campos_para_atualizar:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar.")

        resultado = colecao.update_one({"codigo": codigo}, {"$set": campos_para_atualizar})

        if resultado.modified_count == 0:
            raise HTTPException(status_code=400, detail="Produto não foi atualizado.")

        return {"message": "Produto atualizado com sucesso.", "codigo": codigo, "atualizacoes": campos_para_atualizar}
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Erro no MongoDB: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")

# Rota DELETE - Remover um produto existente
@app.delete("/produtos/{codigo}", status_code=200)
async def deletar_produto(codigo: int):
    try:
        resultado = colecao.delete_one({"codigo": codigo})

        if resultado.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Produto não encontrado.")

        return {"message": "Produto deletado com sucesso.", "codigo": codigo}
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=f"Erro no MongoDB: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")
