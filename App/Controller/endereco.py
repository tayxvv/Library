from fastapi import APIRouter

endereco_router = APIRouter(tags=["Endereço"])

# Simulando uma lista de endereços em memória (substitua com um banco de dados real)
enderecos = []

@endereco_router.post('/endereco/create', summary="Criar um novo endereço")
async def criarEndereco(endereco: dict):
    enderecos.append(endereco)
    return {"message": "Endereço criado com sucesso"}

@endereco_router.get('/endereco/list', summary="Listar todos os endereços")
async def listarEnderecos():
    return enderecos

@endereco_router.get('/endereco/get/{endereco_id}', summary="Obter informações de um endereço pelo ID")
async def obterEndereco(endereco_id: int):
    if endereco_id < len(enderecos):
        return enderecos[endereco_id]
    else:
        return {"message": "Endereço não encontrado"}

@endereco_router.put('/endereco/update/{endereco_id}', summary="Atualizar informações de um endereço pelo ID")
async def atualizarEndereco(endereco_id: int, novo_endereco: dict):
    if endereco_id < len(enderecos):
        enderecos[endereco_id] = novo_endereco
        return {"message": "Endereço atualizado com sucesso"}
    else:
        return {"message": "Endereço não encontrado"}

@endereco_router.delete('/endereco/delete/{endereco_id}', summary="Excluir um endereço pelo ID")
async def deletarEndereco(endereco_id: int):
    if endereco_id < len(enderecos):
        endereco_removido = enderecos.pop(endereco_id)
        return {"message": "Endereço removido com sucesso", "endereco_removido": endereco_removido}
    else:
        return {"message": "Endereço não encontrado"}