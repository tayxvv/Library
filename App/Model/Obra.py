class Obra:
    def __init__(self, lingua, midia, nacionalidade, id_autor, ano, idEditora):
        self.lingua = lingua
        self.midia = midia
        self.nacionalidade = nacionalidade
        self.id_autor = id_autor
        self.ano = ano
        self.idEditora = idEditora

    def inserirObra(self, lingua, midia, nacionalidade, id_autor, ano, idEditora):
        return Obra(lingua, midia, nacionalidade, id_autor, ano, idEditora)
    
    def alterarObra(self, lingua, midia, nacionalidade, id_autor, ano, idEditora):
        self.lingua = lingua
        self.midia = midia
        self.nacionalidade = nacionalidade
        self.id_autor = id_autor
        self.ano = ano
        self.idEditora = idEditora

    def deletarObra(self, id):
        return

    def procurarObra(self, id, nome):
        return
    
    def listarObra(self, id):
        return