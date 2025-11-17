from access_fun import login, resetPassword, updateUser
from db.access_file_user import insert_user, delete_user

# Função que exibe o menu do usuário logado
def user_menu(user: str):
    while True:
        print(f"\n== MENU DO USUÁRIO ({user}) ==")
        print("1 - Atualizar Senha")
        print("2 - Alterar Nome de Usuário")
        print("3 - Excluir Conta")
        print("0 - Logout")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            # Alterar a senha do usuário
            print("\n--- ALTERAR SENHA ---")
            pwd = input("Senha atual: ")
            new_pwd = input("Nova senha: ")
            print(resetPassword(user, pwd, new_pwd))

        elif opc == "2":
            # Alterar o nome de usuário
            print("\n--- ALTERAR NOME DE USUÁRIO ---")
            pwd = input("Senha atual: ")
            new_user = input("Novo nome de usuário: ")
            result = updateUser(user, pwd, new_user)
            print(result)

            # Se alterar o nome com sucesso, atualiza o usuário logado
            if "sucesso" in result.lower():
                user = new_user

        elif opc == "3":
            # Excluir a conta do usuário
            confirm = input("Digite SIM para confirmar: ").upper()
            if confirm == "SIM":
                delete_user(user)
                print("Conta excluída com sucesso!")
                return
            else:
                print("Operação cancelada.")

        elif opc == "0":
            # Logout do usuário
            print("Saindo da conta...")
            return
        
        else:
            print("Opção inválida.")


# Função principal que exibe o menu inicial
def main():
    while True:
        print("\n== MENU PRINCIPAL ==")
        print("1 - Cadastrar Usuário")
        print("2 - Fazer Login")
        print("0 - Sair")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            # Permite cadastrar um novo usuário
            # É possível cadastrar mais de um de usuários repetindo esta opção
            print("\n--- CADASTRAR USUÁRIO ---")
            user = input("Usuário: ")
            pwd = input("Senha: ")
            print(insert_user(user, pwd))

        elif opc == "2":
            # Permite login de um usuário existente
            print("\n--- LOGIN ---")
            user = input("Usuário: ")
            pwd = input("Senha: ")

            if login(user, pwd):
                print("Login realizado com sucesso!")
                user_menu(user)
            else:
                print("Usuário ou senha inválidos.")

        elif opc == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()