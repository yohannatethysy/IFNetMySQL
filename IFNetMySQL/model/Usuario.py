import mysql.connector
from database.configDB import config

class Usuario():
    def __init__(self, nome, email, senha):

        self.nome = nome
        self.email = email
        self.senha = senha
        
    def inserirUsuario(self, nome, email, senha):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TB_Usuario VALUES(?,?, ?)", (nome, email, senha))
        conn.commit()
        conn.close()

    def listarUsuarios(self):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM TB_Usuario")

        for linha in cursor.fetchall():
            print(linha)

        conn.commit()
        conn.close()
        
    def  deletarUsuario ( self, email, senha):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor() 
        senhaC = self.senha
        se (senha ==  senhaC):
            cursor.execute ( "" "
                DELETE FROM tb_usuario 
                ONDE email =?
                "" " , (email))
         conn.commit ()
         conn.close ()
                            
    def  __str__ (self):
        retorno  " Usuario %s"  % (self.nome)

    def  __repr__ (self):
        retornar a  si mesmo . __str__ ()
