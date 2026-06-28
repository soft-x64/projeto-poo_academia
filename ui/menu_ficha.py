def sub_menu_ficha(ficha_service, item_service, exercicio_service):
    while True:
        print("\n--- GERENCIAR FICHAS ---")
        print("1. Criar | 2. Listar/Abrir | 3. Excluir | 4. Voltar")
        opcao = input("Escolha: ")
        
        if opcao == "1":
            id_aluno = input("ID Aluno: ")
            print("Digite a data no formato DD/MM/AAAA")
            ini = input("Início: ")
            ven = input("Vencimento: ")
            try:
                f_id = ficha_service.criar_ficha(id_aluno, ini, ven)
                print(f"Ficha criada! ID: {f_id}")
            except Exception as e:
                print(f"[!] Erro: {e}")

        elif opcao == "2":
            fichas = ficha_service.listar_todas()
            if not fichas:
                print("\n[!] Nenhuma ficha cadastrada.")
            else:
                print("\n--- Fichas Cadastradas ---")
                for f in fichas:
                    print(f"ID: {f[0]} | Aluno ID: {f[1]} | Início: {f[2]} | Venc: {f[3]}")
                # Aqui você pode adicionar a lógica para abrir a ficha específica se desejar

        elif opcao == "3":
            id_del = input("ID da ficha para excluir: ")
            if id_del.isdigit():
                if ficha_service.excluir(id_del):
                    print("Ficha excluída com sucesso!")
                else:
                    print("[!] Ficha não encontrada.")
            else:
                print("[!] ID inválido.")
                
        elif opcao == "4":
            break
