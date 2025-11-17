import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).parent.resolve()
DIR_PATH = BASE_PATH / 'users.json'

df = pd.read_json(DIR_PATH, encoding='utf-8')

#CRUD -> CREATE, READ, UPDATE, DELETE
def insert_user(user, password):
    '''
    Insere um novo usuário no arquivo JSON
    - Verifica se o usuário já existe
    - Cria um novo ID incremental
    - Salva a nova linha no DataFrame e atualiza o arquivo JSON

    Retorna:
        'Usuário já se encontra cadastrado!' caso o usuário exista
        Caso contrário, insere normalmente
    '''
    if find_by_user(user).empty:
        global df
        df_new = pd.DataFrame({
            "id": int(df['id'].max()) + 1,
            "user": [user],
            "password": [password]
        })
        
        df = pd.concat([df, df_new], ignore_index=True)
        df.to_json('./users.json', force_ascii=False, indent=4, orient='records')
        
    return 'Usuário já se encontra cadastrado!'

def update_user(user, new_password):
    '''
    Atualiza a senha de um usuário existente
        - Localiza o usuário no DataFrame
        - Substitui a senha antiga pela nova
        - Salva novamente o JSON

    Retorna:
        None em caso de sucesso
        Mensagem de erro em caso de exceção
    '''
    try:
        df.loc[df['user'] == user, 'password'] = new_password
        df.to_json('./users.json', force_ascii=False, indent=4, orient='records')
    except:
        return 'Error: Exception for update_user'
    

def delete_user(user):
    '''
    Remove um usuário do arquivo JSON
        - Marca a linha como None (nula)
        - Remove as linhas nulas com dropna()
        - Reajusta a coluna ID para manter tipo inteiro
        - Salva novamente no JSON

    Retorna:
        None em caso de sucesso.
        Mensagem de exceção em caso de falha
    '''
    try:
        df.loc[df['user'] == user, :] = None
        df.dropna(inplace=True)
        df['id'] = df['id'].astype(int)
        df.to_json('./users.json', force_ascii=False, indent=4, orient='records')
    except:
        return 'Error: Exception for delete_user'

def find_by_user(user: str):
    return df[df['user'] == user]