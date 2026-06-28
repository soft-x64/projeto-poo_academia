from models.aparelho import Aparelho

def sub_menu_aparelho(aparelho_service):
    while True:
        print("\n--- GERENCIAR APARELHOS ---")
        print("1. Cadastrar | 2. Listar | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do Aparelho: ")
            grupo = input("Grupo Muscular: ")
            novo_aparelho = Aparelho(nome=nome, grupo_muscular=grupo)
            aparelho_service.cadastrar(novo_aparelho)
            print("Aparelho cadastrado com sucesso!")
        
        elif opcao == "2":
            print("\n--- LISTA DE APARELHOS ---")
            for a in aparelho_service.listar_todos():
                print(f"ID: {a.id} | Nome: {a.nome} | Grupo: {a.grupo_muscular}")

        elif opcao == "3":
            try:
                id_excluir = int(input("ID para excluir: "))
                aparelho_service.excluir(id_excluir)
            except ValueError:
                print("ID inválido!")
        elif opcao == "4":
            break
