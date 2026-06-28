from models.exercicio import Exercicio

def sub_menu_exercicio(exercicio_service, aparelho_service):
    while True:
        print("\n--- GERENCIAR EXERCÍCIOS ---")
        print("1. Cadastrar | 2. Listar | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do Exercício: ")
            grupo = input("Grupo Muscular: ")
            
            # Listamos os aparelhos para o usuário escolher o ID
            print("\nAparelhos disponíveis:")
            for a in aparelho_service.listar_todos():
                print(f"ID: {a.id} | {a.nome}")
            
            id_aparelho = input("Digite o ID do aparelho para este exercício: ")
            
            novo_exercicio = Exercicio(nome=nome, grupo_muscular=grupo, id_aparelho=id_aparelho)
            exercicio_service.cadastrar(novo_exercicio)
            print("Exercício cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- LISTA DE EXERCÍCIOS ---")
            for e in exercicio_service.listar_todos():
                print(f"ID: {e.id} | Nome: {e.nome} | Grupo: {e.grupo_muscular} | Aparelho ID: {e.id_aparelho}")

        elif opcao == "3":
            try:
                id_excluir = int(input("ID para excluir: "))
                exercicio_service.excluir(id_excluir)
            except ValueError:
                print("ID inválido!")
        elif opcao == "4":
            break
