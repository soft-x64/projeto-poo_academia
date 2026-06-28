from models.exercicio import Exercicio

def sub_menu_exercicio(exercicio_service, aparelho_service):
    while True:
        print("\n--- GERENCIAR EXERCÍCIOS ---")
        print("1. Cadastrar | 2. Listar | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            print("\n--- Aparelhos Disponíveis ---")
            aparelhos = aparelho_service.listar_todos()
            for a in aparelhos:
                print(f"ID: {a.id} | Nome: {a.nome}")
            
            nome = input("Nome: ")
            grupo = input("Grupo Muscular: ")
            descricao = input("Descrição Áudio: ")
            id_aparelho = int(input("ID Aparelho: "))

            novo_exercicio = Exercicio(
                nome=nome, 
                grupomuscular=grupo, 
                descricaoaudio=descricao, 
                idaparelho=id_aparelho
            )
            exercicio_service.cadastrar(novo_exercicio)
            print("Exercício cadastrado com sucesso!")

        elif opcao == "2":
            exercicios = exercicio_service.listar_todos()
            if not exercicios:
                print("[!] Nenhum exercício cadastrado.")
            else:
                for e in exercicios:
                    print(f"ID: {e.id} | Nome: {e.nome} | Grupo: {e.grupomuscular} | Aparelho ID: {e.idaparelho}")

        elif opcao == "3":
            id_exercicio = int(input("Digite o ID do exercício para excluir: "))
            exercicio_service.excluir(id_exercicio)

        elif opcao == "4":
            break
