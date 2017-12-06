import mysql.connector
from database.configDB import config

class Usuario():
    def __init__(self, nome, email):

        self.nome = nome
        self.email = email

    def inserirUsuario(self, nome, email):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TB_Usuario VALUES(%s,%s)", (nome, email))
        conn.commit()
        conn.close()

    def listarUsuario(self):
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM TB_Usuario")

        for linha in cursor.fetchall():
            print(linha)

        conn.commit()
        conn.close()
