from datetime import datetime as dt
from db.access_file_user import find_by_user, update_user, df

def login(user: str, password: str) -> bool:
    '''
    Verifica se o login é válido.
    Parâmetros:
        - user (str): nome do usuário
        - password (str): senha do usuário

    Retorno:
        - True se credenciais corretas, False caso contrário
    '''
    result = find_by_user(user)
    
    if result.empty:
        return False

    saved_password = result.iloc[0]["password"]
    return saved_password == password

def resetPassword(user: str, password: str, new_password: str) -> str:
    '''
    Redefine a senha do usuário.
    Parâmetros:
        - user (str): nome do usuário
        - password (str): senha atual
        - new_password (str): nova senha

    Retorno:
        - Mensagem de sucesso ou erro
    '''
    if not login(user, password):
        return "Erro: credenciais inválidas!"

    update_user(user, new_password)
    return "Senha atualizada com sucesso!"

def updateUser(user: str, password: str, new_user: str) -> str:
    '''
    Modifica o nome do usuário.
    Parâmetros:
        - user (str): nome atual do usuário
        - password (str): senha do usuário
        - new_user (str): novo nome de usuário

    Retorno:
        - Mensagem de sucesso ou erro
    '''
    try:
        if not login(user, password):
            return "Erro: credenciais inválidas!"

        if not find_by_user(new_user).empty:
            return "Erro: este nome já está em uso!"

        df.loc[df["user"] == user, "user"] = new_user
        df.to_json('./users.json', force_ascii=False, indent=4, orient='records')

        return "Usuário atualizado com sucesso!"

    except Exception as e:
        now = dt.now()
        print(f"log:[{now.date()} - {now.time()}]: Erro no servidor! Detalhe: {e}")
        return "Erro: não foi possível atualizar o usuário."