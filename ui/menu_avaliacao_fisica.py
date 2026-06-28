def sub_menu_avaliacao_fisica(avaliacao_fisica_service):
    while True:
        print("\n--- AVALIAÇÃO FÍSICA ---")
        print("1. Registrar | 2. Ver Histórico | 3. Voltar")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            aluno_id = input("ID do Aluno: ")
            instrutor_id = input("ID do Instrutor: ")
            peso = input("Peso (ex: 80.5): ")
            altura = input("Altura (ex: 1.75): ")
            avaliacao_fisica_service.registrar(aluno_id, instrutor_id, peso, altura)
            print("Avaliação registrada!")
        elif opcao == "2":
            aluno_id = input("ID do Aluno para buscar: ")
            historico = avaliacao_fisica_service.listar_do_aluno(aluno_id)
            for av in historico:
                print(f"Data: {av.data} | Peso: {av.peso}kg | IMC: {av.imc}")
        elif opcao == "3":
            break
