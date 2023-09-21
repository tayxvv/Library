class Endereco:
    def __init__(self, id, rua, numero, bairro, cidade, estado, cep):
        self.id = id
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def inserirEndereco(self, rua, numero, bairro, cidade, estado, cep):
        return Endereco(rua, numero, bairro, cidade, estado, cep)
    
    def alterarEndereco(self, id, rua, numero, bairro, cidade, estado, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        return
    
    def deletarEndereco(self, id):
        return
    
    def procurarEndereco(self, id, nome):
        return
    
    def listarEndereco(self, id):
        return    