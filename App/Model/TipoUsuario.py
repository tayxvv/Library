class TipoUsuario:
    def __init__(self, nome):
        self.nome = nome

    def inserirTipoUsuario(self, nome):
        return TipoUsuario(nome)
    
    def alterarTipoUsuario(self, id, nome):
        self.id = id
        self.nome = nome
        
        return
    
    def deletarTipoUsuario(self, id):
        return
    
    def procurarTipoUsuario(self, id, nome):
        return
    
    def listarTipoUsuario(self, id):
        return    