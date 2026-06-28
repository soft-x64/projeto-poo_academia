def sub_menu_aparelho(aparelho_service):
    while True:
        print("\n--- GERENCIAR APARELHOS ---")
        print("1. Cadastrar | 2. Listar | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            grupo = input("Grupo Muscular: ")
            aparelho_service.cadastrar(nome, grupo)
            print("Aparelho cadastrado com sucesso!")
            
        elif opcao == "2":
            lista = aparelho_service.listar_todos()
            if not lista:
                print("------------------------------")
                print("\nNenhum aparelho cadastrado.")
            else:
                for a in lista:
                    print(f"ID: {a.id} | Nome: {a.nome} | Grupo: {a.grupoMuscular}")
                    
        elif opcao == "3":
            id_del = input("Digite o ID do aparelho para excluir: ")
            try:
                aparelho_service.excluir(id_del)
                print("Aparelho excluído com sucesso!")
            except Exception as e:
                print(f"Erro ao excluir: {e}. (Verifique se não há exercícios usando este aparelho).")
                
        elif opcao == "4":
            break
        else:
            print("\n[!] Opção inválida!")  
