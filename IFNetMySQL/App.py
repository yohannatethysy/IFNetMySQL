import mysql.connector
from database.configDB import config
from database.RedeSocialDAO import RedeSocialDAO
from model.Usuario import Usuario

def exibirMenu():
    print("Rede Social \n"
        " 1 - Definir nome da rede social.\n"
        " 2 - Cadastrar usuário.\n"
        " 3 - Excluir conta usuário \n"
        " 0 - Sair")

def main():
    op = int(input("informe a opção:"))

    while True:
        if op == 1 :
            nomeRD = input("informe o nome da rede social: \n")
            descricao = input("descreva a rede social: ")
            RedeSocialDAO()

        elif op ==2 :
            nome = input("informe seu nome: \n")
            email = input("informe seu email: \n")
            u = Usuario(nome, email)
            u.inserirUsuario(nome, email)
        
        elif op == 3 :
            email = input("informe o email: \n")
            senha = input("informe a senha: \n")
            u.deletarUsuario (email, senha)
            
if __name__ == '__main__':
    main()
