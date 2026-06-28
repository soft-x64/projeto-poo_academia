from models.aluno import Aluno

def sub_menu_aluno(aluno_service):
    while True:
        print("\n--- GERENCIAR ALUNOS ---")
        print("1. Cadastrar | 2. Listar | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")
        if opcao == "1":
            aluno = Aluno(
                nome=input("Nome: "), 
                cpf=input("CPF: "), 
                email=input("E-mail: "), 
                telefone=input("Telefone: "), 
                objetivo=input("Objetivo: ")
            )
            aluno_service.cadastrar(aluno)
            print("Sucesso!")
        elif opcao == "2":
            # POLIMORFISMO AQUI: chama o método definido na classe base ou herdada
            for a in aluno_service.listar_todos():
                print(f"ID: {a.id} | {a.exibir_perfil()} | Tel: {a._telefone}")
        elif opcao == "3":
            try:
                id_excluir = int(input("ID para excluir: "))
                aluno_service.excluir(id_excluir)
                print("Excluído!")
            except:
                print("ID inválido!")
        elif opcao == "4": break
