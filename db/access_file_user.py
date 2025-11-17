import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).parent.resolve()
DIR_PATH = BASE_PATH / 'users.json'

df = pd.read_json(DIR_PATH, encoding='utf-8')

#CRUD -> CREAT, READ, UPDATE, DELETE
def insert_user(user, password):
    if find_by_user(user).empty:
        global df
        df_new = pd.DataFrame({
            "id" : df['id'].max() + 1,
            "user" : [user],
            "password" : [password]
        })

        df = pd.concat([df, df_new], ignore_index=True)
        df.to_json('./users.json', force_ascii=False, indent=4, orient='records')
        
    return 'Usuário já se encontra cadastrado!'

def update_user(user, new_password):
    try:
        df.loc[df[df['user'] == user], 'password'] = new_password
        df.to_json('./user.json', force_ascii=False, indent=4, orient='records')
        df['id'] = df['id'].astype(int)
        df.to_json('./users.json', force_ascii=False, indent=4, orient='records')
    except:
        return 'Error: Exceptio for update_user'

def delete_user(user):
    try:
        df.loc[df['user'] == user, 'password'] = None
        df.dropna(inplace=True)
        df.to_json('./users.json', force_ascii=False, indent=4, orient='records')
    except:
        return 'Error: Exception for delete_user'

def find_by_user(user: str):
    return df[df['user'] == user]