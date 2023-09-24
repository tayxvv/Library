from App.dependencias.config import setting
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Autor(setting.DBBaseModel):

    __tablename__ = "autor"

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    # codigoUsuario = Column(Integer, ForeignKey("usuario.codigo"))
    # itemAutor = relationship("ItemAutor", back_populates="autor")


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