from fastapi import APIRouter

emprestimo_router = APIRouter(tags=["Empréstimo"])

# Simulando uma lista de empréstimos em memória (substitua com um banco de dados real)
emprestimos = []

@emprestimo_router.post('/emprestimo/create', summary="Criar um novo empréstimo de livro")
async def criarEmprestimo(emprestimo: dict):
    emprestimos.append(emprestimo)
    return {"message": "Empréstimo de livro criado com sucesso"}

@emprestimo_router.get('/emprestimo/list', summary="Listar todos os empréstimos de livros")
async def listarEmprestimos():
    return emprestimos

@emprestimo_router.get('/emprestimo/get/{emprestimo_id}', summary="Obter informações de um empréstimo de livro pelo ID")
async def obterEmprestimo(emprestimo_id: int):
    if emprestimo_id < len(emprestimos):
        return emprestimos[emprestimo_id]
    else:
        return {"message": "Empréstimo de livro não encontrado"}

@emprestimo_router.put('/emprestimo/update/{emprestimo_id}', summary="Atualizar informações de um empréstimo de livro pelo ID")
async def atualizarEmprestimo(emprestimo_id: int, novo_emprestimo: dict):
    if emprestimo_id < len(emprestimos):
        emprestimos[emprestimo_id] = novo_emprestimo
        return {"message": "Empréstimo de livro atualizado com sucesso"}
    else:
        return {"message": "Empréstimo de livro não encontrado"}

@emprestimo_router.delete('/emprestimo/delete/{emprestimo_id}', summary="Excluir um empréstimo de livro pelo ID")
async def deletarEmprestimo(emprestimo_id: int):
    if emprestimo_id < len(emprestimos):
        emprestimo_removido = emprestimos.pop(emprestimo_id)
        return {"message": "Empréstimo de livro removido com sucesso", "emprestimo_removido": emprestimo_removido}
    else:
        return {"message": "Empréstimo de livro não encontrado"}