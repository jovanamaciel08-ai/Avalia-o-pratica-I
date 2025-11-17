from access_fun import login, resetpassword, updateUser
from database import *

print("-- Sistema de Login --")

user = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

if login(user, password):
    print(f"f\n Login sucedido! Bem-vindo, {user}.")

    while True:
        print("\nO que deseja?")
        print("1 - Redefinir senha")
        print("2 - Alterar nome do usuário")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            new_password = input("Digite a nova senha: ")
            print(resetpassword(user, password, new_password))
            password = new_password
        
        elif opcao == "2":
            new_user = input("Digite o novo nome de usuário: ")
            print(updateUser(user, password, new_user))
            user = new_user

        elif opcao == "3":
            print("Encerrando sistema. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")
    
else:
    print("\n Usuário ou senha incorretos. Tente novamente.")

'''
Desenvolver um pequeno projeto de interação com o usuário
ultilizando todas as funções que foram desenvolvidas no módulo
access_fun.py

O usuario deve:
    - fazer login
    - redefinir senha
    - modificar nome do usuario
'''
