from models.instrutor import Instrutor

def sub_menu_instrutor(instrutor_service):
    while True:
        print("\n--- GERENCIAR INSTRUTORES ---")
        print("1. Cadastrar Instrutor")
        print("2. Listar Instrutores")
        print("3. Excluir Instrutor")
        print("4. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome Completo: ")
            cpf = input("CPF: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            especialidade = input("Especialidade: ")
            
            # Cria o objeto Instrutor e envia para o service
            novo_instrutor = Instrutor(
                nomecompleto=nome, 
                cpf=cpf, 
                email=email, 
                telefone=telefone, 
                especialidade=especialidade
            )
            instrutor_service.cadastrar(novo_instrutor)
            print("Instrutor cadastrado com sucesso!")

        elif opcao == "2":
            instrutores = instrutor_service.listar_todos()
            print("\n--- LISTA DE INSTRUTORES ---")
            for i in instrutores:
                print(f"ID: {i.id} | Nome: {i.nomecompleto} | Especialidade: {i.especialidade}")

        elif opcao == "3":
            try:
                id_instrutor = int(input("Digite o ID do instrutor que deseja excluir: "))
                instrutor_service.excluir(id_instrutor)
            except ValueError:
                print("Erro: O ID deve ser um número inteiro.")

        elif opcao == "4":
            break
        else:
            print("Opção inválida, tente novamente.")
