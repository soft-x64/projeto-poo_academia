from models.ficha_treino import FichaTreino

def sub_menu_ficha(ficha_service, item_service, exercicio_service):
    while True:
        print("\n--- GERENCIAR FICHAS ---")
        print("1. Criar | 2. Listar | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            id_aluno = input("ID Aluno: ")
            data_inicio = input("Início (DD/MM/AAAA): ")
            data_vencimento = input("Vencimento (DD/MM/AAAA): ")
            
            # Usamos o nome correto do atributo (id_aluno, data_inicio...)
            nova_ficha = FichaTreino(id_aluno=id_aluno, data_inicio=data_inicio, data_vencimento=data_vencimento)
            ficha_service.criar(nova_ficha)
            print("Ficha criada com sucesso!")

        elif opcao == "2":
            print("\n--- Fichas Cadastradas ---")
            for f in ficha_service.listar_todas():
                print(f"ID: {f.id} | Aluno ID: {f.id_aluno} | Início: {f.data_inicio} | Venc: {f.data_vencimento}")

        elif opcao == "3":
            try:
                id_excluir = int(input("ID para excluir: "))
                ficha_service.excluir(id_excluir)
            except ValueError:
                print("ID inválido!")
        elif opcao == "4":
            break
