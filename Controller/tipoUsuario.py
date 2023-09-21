from fastapi import APIRouter

tipo_usuario_router = APIRouter(tags=["Tipo de Usuário"])

# Simulando uma lista de tipos de usuário em memória (substitua com um banco de dados real)
tipos_usuario = []

@tipo_usuario_router.post('/tipoUsuario/create', summary="Criar um novo tipo de usuário")
async def criarTipoUsuario(tipo_usuario: dict):
    tipos_usuario.append(tipo_usuario)
    return {"message": "Tipo de usuário criado com sucesso"}

@tipo_usuario_router.get('/tipoUsuario/list', summary="Listar todos os tipos de usuário")
async def listarTiposUsuario():
    return tipos_usuario

@tipo_usuario_router.get('/tipoUsuario/get/{tipo_usuario_id}', summary="Obter informações de um tipo de usuário pelo ID")
async def obterTipoUsuario(tipo_usuario_id: int):
    if tipo_usuario_id < len(tipos_usuario):
        return tipos_usuario[tipo_usuario_id]
    else:
        return {"message": "Tipo de usuário não encontrado"}

@tipo_usuario_router.put('/tipoUsuario/update/{tipo_usuario_id}', summary="Atualizar informações de um tipo de usuário pelo ID")
async def atualizarTipoUsuario(tipo_usuario_id: int, novo_tipo_usuario: dict):
    if tipo_usuario_id < len(tipos_usuario):
        tipos_usuario[tipo_usuario_id] = novo_tipo_usuario
        return {"message": "Tipo de usuário atualizado com sucesso"}
    else:
        return {"message": "Tipo de usuário não encontrado"}

@tipo_usuario_router.delete('/tipoUsuario/delete/{tipo_usuario_id}', summary="Excluir um tipo de usuário pelo ID")
async def deletarTipoUsuario(tipo_usuario_id: int):
    if tipo_usuario_id < len(tipos_usuario):
        tipo_usuario_removido = tipos_usuario.pop(tipo_usuario_id)
        return {"message": "Tipo de usuário removido com sucesso", "tipo_usuario_removido": tipo_usuario_removido}
    else:
        return {"message": "Tipo de usuário não encontrado"}

