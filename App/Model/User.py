class User:
    def __init__(self, id, tipoUsuario, nome, idade, email, sexo):
        self.id = id
        self.tipoUsuario = tipoUsuario
        self.nome = nome
        self.idade = idade
        self.email = email
        self.sexo = sexo

    def inserirTipoUsuario(self, tipoUsuario, nome, idade, email, sexo):
        return User(tipoUsuario, nome, idade, email, sexo)
    
    def alterarTipoUsuario(self, id, tipoUsuario, nome, idade, email, sexo):
        self.id = id
        self.tipoUsuario = tipoUsuario
        self.nome = nome
        self.idade = idade
        self.email = email
        self.sexo = sexo
        return
    
    def deletarTipoUsuario(self, id):
        return
    
    def procurarTipoUsuario(self, id, nome):
        return
    
    def listarTipoUsuario(self, id):
        return    