
def exibir_menu_principal(aluno_service, instrutor_service, aparelho_service, exercicio_service, ficha_service, avaliacao_service):
    while True:
        print("\n--- SISTEMA DE GERENCIAMENTO DE ACADEMIA ---")
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Instrutores")
        print("3. Gerenciar Aparelhos")
        print("4. Gerenciar Exercícios")
        print("5. Gerenciar Fichas de Treino")
        print("6. Gerenciar Avaliações Físicas")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Exemplo de chamada: gerenciar_alunos(aluno_service)
            print("Menu de Alunos...")
        elif opcao == "2":
            print("Menu de Instrutores...")
        # ... outros elifs para cada serviço ...
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
