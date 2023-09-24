from fastapi import APIRouter

obra_router = APIRouter(tags=["Obra"])

# Simulando uma lista de obras em memória (substitua com um banco de dados real)
obras = []

@obra_router.post('/obra/create', summary="Criar uma nova obra (livro)")
async def criarObra(obra: dict):
    obras.append(obra)
    return {"message": "Obra (livro) criada com sucesso"}

@obra_router.get('/obra/list', summary="Listar todas as obras (livros)")
async def listarObras():
    return obras

@obra_router.get('/obra/get/{obra_id}', summary="Obter informações de uma obra (livro) pelo ID")
async def obterObra(obra_id: int):
    if obra_id < len(obras):
        return obras[obra_id]
    else:
        return {"message": "Obra (livro) não encontrada"}

@obra_router.put('/obra/update/{obra_id}', summary="Atualizar informações de uma obra (livro) pelo ID")
async def atualizarObra(obra_id: int, nova_obra: dict):
    if obra_id < len(obras):
        obras[obra_id] = nova_obra
        return {"message": "Obra (livro) atualizada com sucesso"}
    else:
        return {"message": "Obra (livro) não encontrada"}

@obra_router.delete('/obra/delete/{obra_id}', summary="Excluir uma obra (livro) pelo ID")
async def deletarObra(obra_id: int):
    if obra_id < len(obras):
        obra_removida = obras.pop(obra_id)
        return {"message": "Obra (livro) removida com sucesso", "obra_removida": obra_removida}
    else:
        return {"message": "Obra (livro) não encontrada"}