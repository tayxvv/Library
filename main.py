import asyncio
import uvicorn
from fastapi import FastAPI
from Controller.login import login_router  # Importe a rota do login
from Controller.autor import autor_router
from Controller.editora import editora_router
from Controller.emprestimo import emprestimo_router
from Controller.endereco import endereco_router
from Controller.obra import obra_router
from Controller.tipoUsuario import tipo_usuario_router

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
    asyncio.run(main())
    print("Olá")