from fastapi import APIRouter

autor_router = APIRouter(tags=["Autor"])

# Simulando uma lista de autores em memória (substitua com um banco de dados real)
autores = []

@autor_router.post('/autor/create', summary="Criar um novo autor")
async def criarAutor(autor: dict):
    autores.append(autor)
    return {"message": "Autor criado com sucesso"}

@autor_router.get('/autor/list', summary="Listar todos os autores")
async def listarAutores():
    return autores

@autor_router.get('/autor/get/{autor_id}', summary="Obter informações de um autor pelo ID")
async def obterAutor(autor_id: int):
    if autor_id < len(autores):
        return autores[autor_id]
    else:
        return {"message": "Autor não encontrado"}

@autor_router.put('/autor/update/{autor_id}', summary="Atualizar informações de um autor pelo ID")
async def atualizarAutor(autor_id: int, novo_autor: dict):
    if autor_id < len(autores):
        autores[autor_id] = novo_autor
        return {"message": "Autor atualizado com sucesso"}
    else:
        return {"message": "Autor não encontrado"}

@autor_router.delete('/autor/delete/{autor_id}', summary="Excluir um autor pelo ID")
async def deletarAutor(autor_id: int):
    if autor_id < len(autores):
        autor_removido = autores.pop(autor_id)
        return {"message": "Autor removido com sucesso", "autor_removido": autor_removido}
    else:
        return {"message": "Autor não encontrado"}