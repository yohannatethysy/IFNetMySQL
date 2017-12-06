import mysql.connector
from database.configDB import config
from database.RedeSocialDAO import RedeSocialDAO
from model.Usuario import Usuario

def exibirMenu():
    print("Rede Social \n"
        " 1 - Definir nome da rede social.\n"
        " 2 - Cadastrar usuário.\n"
        " 0 - Sair")

def main():
    op = int(input("informe a opção:"))

    while True:
        if op == 1 :
            nomeRD = input("informe o nome da rede social: \n")
            RedeSocialDAO()

        if op ==2 :
            nome = input("informe seu nome: \n")
            email = input("informe seu email: \n")
            u = Usuario(nome, email)
            u.inserirUsuario(nome, email)

if __name__ == '__main__':
    main()
