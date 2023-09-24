class Emprestimo:

    def __init__(self, data_emprestimo, data_devolucao, livro, usuario):
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.livro = livro
        self.usuario = usuario

    def inserirEmprestimo(self, data_emprestimo, data_devolucao, livro, usuario):
        return Emprestimo(data_emprestimo, data_devolucao, livro, usuario)

    def alterarEmprestimo(self, id, data_emprestimo, data_devolucao, livro, usuario):
        self.id = id
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.livro = livro
        self.usuario = usuario

    def excluirEmprestimo(self, id):
        return

    def listarEmprestimo(self, id):
        return
    
    def consultarEmprestimo(self, id):
        return