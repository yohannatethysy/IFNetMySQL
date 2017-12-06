import mysql.connector
from database.configDB import config

conn = mysql.connector.connect(**config)

try:

    def main():

        conn = mysql.connector.connect(**config)

        cursor = conn.cursor()

        # criando as tabelas
        cursor.execute("CREATE TABLE TB_Usuario(id INTEGER PRIMARY KEY, nome VARCHAR(20), email VARCHAR(30))")

        cursor.execute("CREATE TABLE TB_rede_social (nomeRD VARCHAR(20), descricao VARCHAR(150)))")

        cursor.close()

        conn.close()

except mysql.connector.Error as err:

    print("Erro no banco de dados.")
