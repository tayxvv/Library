import asyncio
import uvicorn
from fastapi import FastAPI
from App.Controller.login import login_router  # Importe a rota do login
from App.Controller.autor import autor_router
from App.Controller.editora import editora_router
from App.Controller.emprestimo import emprestimo_router
from App.Controller.endereco import endereco_router
from App.Controller.obra import obra_router
from App.Controller.tipoUsuario import tipo_usuario_router
from App.dependencias.dep import get_session
from App.Model.Autor import Autor
from criarTabelas import create_tables

from sqlalchemy.orm import Session

session = Session()

app = FastAPI()

app.include_router(login_router)  # Inclua a rota do login com um prefixo

app.include_router(autor_router)

app.include_router(editora_router)

app.include_router(emprestimo_router)

app.include_router(endereco_router)

app.include_router(obra_router)

app.include_router(tipo_usuario_router)

async def main():
    config = uvicorn.Config("main:app", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    
    await server.serve()

if __name__ == "__main__":
    connection = get_session()
    asyncio.run(main(connection))
    print("Olá")