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
from sqlalchemy import select
import bcrypt
import jwt
from datetime import datetime, timedelta

db_session = Session()

SECRET_KEY = 'chaveSuperSecreta'

login_router = APIRouter(tags=["Login"])

@login_router.post('/login', summary="Registrar usuários com login")
async def listarLogin(item: usuarioSchema, db: AsyncSession = Depends(get_session)):
    output = select(Login).where(Login.username == item.username)
    resultado = await db.execute(output)
    info_login = resultado.scalars().first()
    if (not info_login):
        return HTTPException(detail="Usuário não encontrado", status_code=404)
    senha_fornecida = item.password.encode('utf-8')
    senha_armazenada = info_login.password
    senhaCorreta = bcrypt.checkpw(senha_fornecida, senha_armazenada)
    if (not senhaCorreta):
        return HTTPException(detail="Usuário ou senha incorreta", status_code=404)
    tempo_de_expiracao = datetime.utcnow() + timedelta(minutes=1)
    encoded = jwt.encode({"some": "payload", "exp": tempo_de_expiracao}, SECRET_KEY, algorithm="HS256")
    #return encoded

    return JSONResponse(content={"token": encoded}, status_code=201)


@login_router.post('/registerLogin', summary="Criar um login para usuários novos")
async def createLogin(item: usuarioSchema, db: AsyncSession = Depends(get_session)):
    try:
        salt = bcrypt.gensalt()
        senha_criptografada = bcrypt.hashpw(item.password.encode('utf-8'), salt)
        #senha_criptografada_hex = senha_criptografada.hex()
        novo_usuario = Login(nome=item.nome, username=item.username, password=senha_criptografada)
        db.add(novo_usuario)
        await db.commit()
        return JSONResponse(content={"message": senha_criptografada}, status_code=201)
    except Exception as e:
        await db.rollback()
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