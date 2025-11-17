from datetime import datetime as dt
from db import *

#Função para realizar o login
def login(user: str, password: str) -> bool:
    '''
    Função para verificar se o login é válido.

    Parâmetros:
        - user (str): nome do usuário
        - password (str): senha do usuário
    
    Retorno: retornará um valor true ou false
    '''
    df = find_by_user(user)
    if df.iloc[0,2] == password:
        return True
    
    return False

#Função para redefinir a senha
def resetpassword(user: str, password: str, new_password: str) -> str:
    '''
    Função para redefinir a senha do usuário.

    Parâmetros:
        - user (str): nome do usuário
        - new_password (str): senha atualizada para registrar
    
    Retorno: Uma String confirmando ou recusando a modificação da senha
    '''
    if login(user, password):
        db[user] = new_password
        return "Senha Alterada!"
    
    return "Error: Credenciais Inválida!"

#Função para modificar o nome do usuário
def updateUser(user: str, password: str, new_user: str) -> object:
    '''
    Função para modificar o nome do usuário.

    Parâmetros:
        - user (str): nome do usuário
        - password (str): senha do usuário
        - new_password (str): novo nome do usuário

    Retorno: confirma a modificação do usuário.
        Caso seja disparado algum erro será gerado um log.
    '''
    try:
        if login(user, password):
            db[new_user] = db.pop(user)
            return 'Usuário atualizou co sucesso!'

    except:
        print(f'log:[{dt.date}] - [{dt.time}]: Error no Servidor!')