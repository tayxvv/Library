import bcrypt
from Library.Connection import Connection

class Login:

    def __init__(self):
        conexaoInstancia = Connection()
        self.conexao = conexaoInstancia.connect()

    def inserirLogin(self, usuario, senha):
        salt = bcrypt.gensalt()
        senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), salt)
        
        sql = "INSERT INTO adm.users (username, password_hash) VALUES (%s, %s) returning user_id;"
        values = (usuario, senha_criptografada)
        connection = self.conexao.cursor()
        connection.execute(sql, values)
        self.conexao.commit()
        version = connection.fetchone()

        return version[0]
    
    def deletarLogin(self, usuario):
        return
    
    def procurarLogin(self, usuario, senha):
        sql = "select * from adm.users where username = %s"
        values = (usuario)
        connection = self.conexao.cursor()
        connection.execute(sql, values)
        self.conexao.commit()
        version = connection.fetchone()

        return version[0]
    
    def listarLogin(self):
        return

    def alterarLogin(self, usuario, senha):
        return    