from fastapi import APIRouter
from Types.ILoginRequest import ILoginRequest
from Library.Entitys.Login import Login

login_router = APIRouter(tags=["Login"])

@login_router.get('/login', summary="Registrar usuários com login")
async def listarLogin():
    login = {
        "username": "aa"
    }

    return login

@login_router.post('/registerLogin', summary="Criar um login para usuários novos")
async def createLogin(login_request: ILoginRequest):
    login = Login()
    retorno = login.inserirLogin()
    # login = {
    #     "username": login_request.userName,
    #     "password": login_request.senha
    # }
    return retorno
    # return login

@login_router.post('/login', summary="fazer validação do login")
async def validateLogin(login_request: ILoginRequest):
    login = Login()
    retorno = login.procurarLogin(login_request.usuario)
    # bcrypt.checkpw(user_input_password.encode('utf-8'), hashed_password)
    login = {
        "username": "aa"
    }

    return login