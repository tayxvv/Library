from App.dependencias.config import setting
from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from ..Schema.usuarioSchema import usuarioSchema
from sqlalchemy.orm import Session

class Login(setting.DBBaseModel):

    __tablename__ = "login"

    codigo = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(LargeBinary, nullable=False)
    # codigoUsuario = Column(Integer, ForeignKey("usuario.codigo"))
    # itemLogin = relationship("ItemLogin", back_populates="Login")

    def __init__(self, nome, username, password):
        self.nome = nome
        self.username = username
        self.password = password

    # def inserirLogin(self, item: usuarioSchema, db: Session):
    #     db_item = Login(**item.model_dump())
    #     db.add(db_item)
    #     db.commit()
    #     db.refresh(db_item)
    #     db.close()
    #     return "inserido"
    
    def alterarLogin(self, id, nome):
        self.id = id
        self.nome = nome
        
        return
    
    def deletarLogin(self, id):
        return
    
    def procurarLogin(self, id, nome):
        return
    
    def listarLogin(self, id):
        return