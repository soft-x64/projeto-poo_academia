from models.instrutor import Instrutor

def sub_menu_instrutor(instrutor_service):
    while True:
        print("\n--- GERENCIAR INSTRUTORES ---")
        print("1. Cadastrar | 2. Listar | 3. Excluir | 4. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- CADASTRAR INSTRUTOR ---")
            nome = input("Nome: ")
            cpf = input("CPF: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            especialidade = input("Especialidade: ")
            
            instrutor_service.cadastrar(Instrutor(nome=nome, cpf=cpf, email=email, telefone=telefone, especialidade=especialidade))
            print("Instrutor cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- LISTA DE INSTRUTORES ---")
            for i in instrutor_service.listar_todos():
                print(f"ID: {i.id} | {i.exibir_perfil()} | Contato: {i._telefone}")

        elif opcao == "3":
            try:
                id_excluir = int(input("Digite o ID do instrutor para excluir: "))
                # O service já cuida da mensagem de sucesso ou erro
                instrutor_service.excluir(id_excluir)
            except ValueError:
                print("Erro: ID inválido. Por favor, digite um número.")

        elif opcao == "4":
            break
        else:
            print("Opção inválida, tente novamente.")
