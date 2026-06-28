from models.exercicio import Exercicio

def sub_menu_exercicio(exercicio_service, aparelho_service):
    while True:
        print("\n--- GERENCIAR EXERCÍCIOS ---")
        print("1. Cadastrar | 2. Listar | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do Exercício: ")
            grupo = input("Grupo Muscular: ")
            
            # Lista os aparelhos disponíveis
            print("\nAparelhos disponíveis:")
            aparelhos = aparelho_service.listar_todos()
            for a in aparelhos:
                print(f"ID: {a.id} | {a.nome}")
            
            id_aparelho_input = input("Digite o ID do aparelho para este exercício: ")
            
            # Validação para evitar erro de banco de dados
            if not nome.strip() or not grupo.strip() or not id_aparelho_input.isdigit():
                print("\n[!] Erro: Nome e Grupo são obrigatórios e o ID do Aparelho deve ser um número válido!")
            else:
                novo_exercicio = Exercicio(
                    nome=nome, 
                    grupo_muscular=grupo, 
                    id_aparelho=int(id_aparelho_input)
                )
                exercicio_service.cadastrar(novo_exercicio)
                print("Exercício cadastrado com sucesso!")
            
        elif opcao == "2":
            print("\n--- LISTA DE EXERCÍCIOS ---")
            for ex in exercicio_service.listar_todos():
                print(f"ID: {ex.id} | Nome: {ex.nome} | Grupo: {ex.grupo_muscular} | Aparelho ID: {ex.id_aparelho}")
        
        elif opcao == "3":
            try:
                id_excluir = int(input("ID do exercício para excluir: "))
                exercicio_service.excluir(id_excluir)
                print("Exercício excluído!")
            except ValueError:
                print("ID inválido!")
            
        elif opcao == "4":
            break
