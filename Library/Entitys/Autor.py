class Autor:

    def __init__(self, nome):
        self.nome = nome

    def inserirAutor(self, nome):
        return Autor(nome)
    
    def alterarAutor(self, id, nome):
        self.id = id
        self.nome = nome
        
        return
    
    def deletarAutor(self, id):
        return
    
    def procurarAutor(self, id, nome):
        return
    
    def listarAutor(self, id):
        return