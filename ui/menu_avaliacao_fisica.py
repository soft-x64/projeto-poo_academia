from models.avaliacao_fisica import AvaliacaoFisica

def sub_menu_avaliacao(avaliacao_service):
    while True:
        print("\n--- GERENCIAR AVALIAÇÕES FÍSICAS ---")
        print("1. Cadastrar | 2. Listar por Aluno | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            id_aluno = input("ID do Aluno: ")
            data = input("Data (DD/MM/AAAA): ")
            peso = input("Peso (kg): ")
            altura = input("Altura (m): ")
            
            nova_av = AvaliacaoFisica(id_aluno=id_aluno, data=data, peso=peso, altura=altura)
            avaliacao_service.cadastrar(nova_av)
            
        elif opcao == "2":
            id_aluno = input("ID do Aluno para buscar: ")
            print("\n--- AVALIAÇÕES DO ALUNO ---")
            for av in avaliacao_service.listar_por_aluno(id_aluno):
                print(f"ID: {av.id} | Data: {av.data} | Peso: {av.peso}kg | Altura: {av.altura}m")
        
        elif opcao == "3":
            id_excluir = int(input("ID da avaliação para excluir: "))
            avaliacao_service.excluir(id_excluir)
            
        elif opcao == "4":
            break
