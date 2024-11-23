# API em Python de Produtos - FastAPI e MongoDB

Esta é uma API de gerenciamento de produtos construída com **FastAPI** e **MongoDB**. A API permite realizar operações CRUD (Criar, Ler, Atualizar e Deletar) sobre um banco de dados MongoDB. A aplicação foi desenvolvida com foco em simplicidade e performance com inteligencia artificial.

---

## Funcionalidades

A API possui as seguintes rotas:

- **GET /produtos**: Retorna a lista de todos os produtos.
- **POST /produtos**: Cria um novo produto.
- **PATCH /produtos/{codigo}**: Atualiza um produto existente.
- **DELETE /produtos/{codigo}**: Remove um produto pelo código.

---

## Tecnologias

- **FastAPI**: Framework para construção de APIs rápidas e eficientes com Python.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenar os dados dos produtos.
- **Docker**: Ferramenta para rodar o MongoDB em container.

---

## Requisitos

- **Python 3.9+**
- **Docker** (para rodar o MongoDB)
- **MongoDB** (Rodando no Docker ou localmente)
- **FastAPI e Uvicorn para a API**

---

## Instalação

### 1. Clonando o Repositório

Clone o repositório para a sua máquina:

```bash
git clone https://github.com/Bitcomiatech/API_Python_IA.git
cd projeto-api-produtos
```
## 2. Instalando Dependências
```bash
pip install fastapi pymongo uvicorn
```
### 3. Rodando o MongoDB com Docker
- **Se você ainda não tem o MongoDB rodando, utilize o Docker para subir o container**
```bash
docker run -d -p 27017:27017 --name mongodb mongo
```
### 4. Executando a API
- **Para iniciar o servidor da API, execute**
```bash
uvicorn main:app --reload
```
- **A aplicação estará disponível em http://127.0.0.1:8000.**

- ## Endpoints

### 1. **GET /produtos**

Retorna todos os produtos cadastrados no MongoDB.

**Resposta**:

```json
{
  "data": [
    {
      "codigo": 1,
      "nome": "Produto 1",
      "quantidade": 10,
      "valor": 199.99
    },
{
      "codigo": 2,
      "nome": "Produto 2",
      "quantidade": 11,
      "valor": 11.99
    }
  ]
}
```

### 2. **POST /produtos**

Cria um novo produto.

**Requisição**:

```json
{
  "codigo": 3,
  "nome": "Produto 3",
  "quantidade": 5,
  "valor": 99.99
}
```
**Resposta**:
```json
{
  "message": "Produto inserido com sucesso.",
  "produto": {
    "codigo": 2,
    "nome": "Produto 2",
    "quantidade": 5,
    "valor": 99.99
  }
}
```

### 3. **PATCH /produtos/{codigo}**

Atualiza um produto existente com base no código.

**Requisição**:

```json
{
  "valor": 120.99
}
```
**Resposta**:
```json
{
  "message": "Produto atualizado com sucesso.",
  "codigo": 2,
  "atualizacoes": {
    "valor": 120.99
  }
}
```

### 4. **DELETE /produtos/{codigo}**

Remove um produto com base no código.

**Resposta**:
```json
{
  "message": "Produto deletado com sucesso.",
  "codigo": 2
}
```
