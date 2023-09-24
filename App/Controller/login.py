from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from Types.ILoginRequest import ILoginRequest
from App.Model.Login import Login
from criarTabelas import create_tables
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from sqlalchemy.orm import Session
from ..Schema.usuarioSchema import usuarioSchema
from App.dependencias.dep import get_session

db_session = Session()

login_router = APIRouter(tags=["Login"])

@login_router.get('/login', summary="Registrar usuários com login")
async def listarLogin():
    login = {
        "username": "aa"
    }

    return login

@login_router.post('/registerLogin', summary="Criar um login para usuários novos")
async def createLogin(item: usuarioSchema, db: AsyncSession = Depends(get_session)):
    try:
        novo_usuario = Login(nome=item.nome, username=item.username, password=item.password)
        db.add(novo_usuario)
        await db.commit()
        return JSONResponse(content={"message": "Login criado com sucesso"}, status_code=201)
    except Exception as e:
        # Você pode adicionar tratamento de exceções específicas aqui
        return HTTPException(detail=str(e), status_code=400)

# @login_router.post('/login', summary="fazer validação do login")
# async def validateLogin(login_request: ILoginRequest):
#     login = Login()
#     retorno = login.procurarLogin(login_request.usuario)
#     # bcrypt.checkpw(user_input_password.encode('utf-8'), hashed_password)
#     login = {
#         "username": "aa"
#     }

#     return login