from models.aluno import Aluno

def sub_menu_aluno(aluno_service):
    while True:
        print("\n--- GERENCIAR ALUNOS ---")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Excluir Aluno")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome Completo: ")
            email = input("E-mail: ")
            contato = input("Contato: ")
            objetivo = input("Objetivo: ")
            
            # Criamos o objeto aqui
            novo_aluno = Aluno(nomecompleto=nome, email=email, contato=contato, objetivo=objetivo)
            
            # Enviamos APENAS o objeto
            aluno_service.cadastrar(novo_aluno)
            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            alunos = aluno_service.listar_todos()
            print("\n--- LISTA DE ALUNOS ---")
            for a in alunos:
                print(f"ID: {a.id} | Nome: {a.nomecompleto} | Objetivo: {a.objetivo} | Contato: {a.contato}")

        elif opcao == "3":
            id_aluno = input("Digite o ID do aluno que deseja excluir: ")
            aluno_service.excluir(int(id_aluno))

        elif opcao == "4":
            break
