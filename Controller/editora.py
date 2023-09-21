from fastapi import APIRouter

editora_router = APIRouter(tags=["Editora"])

# Simulando uma lista de editoras em memória (substitua com um banco de dados real)
editoras = []

@editora_router.post('/editora/create', summary="Criar uma nova editora")
async def criarEditora(editora: dict):
    editoras.append(editora)
    return {"message": "Editora criada com sucesso"}

@editora_router.get('/editora/list', summary="Listar todas as editoras")
async def listarEditoras():
    return editoras

@editora_router.get('/editora/get/{editora_id}', summary="Obter informações de uma editora pelo ID")
async def obterEditora(editora_id: int):
    if editora_id < len(editoras):
        return editoras[editora_id]
    else:
        return {"message": "Editora não encontrada"}

@editora_router.put('/editora/update/{editora_id}', summary="Atualizar informações de uma editora pelo ID")
async def atualizarEditora(editora_id: int, nova_editora: dict):
    if editora_id < len(editoras):
        editoras[editora_id] = nova_editora
        return {"message": "Editora atualizada com sucesso"}
    else:
        return {"message": "Editora não encontrada"}

@editora_router.delete('/editora/delete/{editora_id}', summary="Excluir uma editora pelo ID")
async def deletarEditora(editora_id: int):
    if editora_id < len(editoras):
        editora_removida = editoras.pop(editora_id)
        return {"message": "Editora removida com sucesso", "editora_removida": editora_removida}
    else:
        return {"message": "Editora não encontrada"}