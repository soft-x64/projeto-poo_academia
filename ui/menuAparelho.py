from models.aparelho import Aparelho
from models.exercicio import Exercicio

def menu_equipamentos(lista_aparelhos, lista_exercicios):
    while True:
        print("\n--- GESTAO DE APARELHOS E EXERCICIOS ---")
        print("1. Cadastrar Aparelho")
        print("2. Listar Aparelhos")
        print("3. Cadastrar Exercicio")
        print("4. Listar Exercicios")
        print("5. Voltar")
        
        opcao = input("Escolha uma opcao: ")
        if opcao == '1':
            print("\n--- Cadastro de Aparelho ---")
            nome = input("Nome do Aparelho (ex: Leg Press): ")
            tipo = input("Tipo/Categoria (ex: Articulado): ")
            cap_carga = input("Capacidade de Carga em kg (Opcional - Enter para pular): ")
            cap_carga = float(cap_carga) if cap_carga else None
            
            aparelho = Aparelho(nome, tipo, cap_carga)
            lista_aparelhos.append(aparelho)
            print(f"Sucesso: Aparelho '{aparelho.nome}' cadastrado!")
            
        elif opcao == '2':
            print("\n--- Aparelhos Disponiveis ---")
            if not lista_aparelhos:
                print("Nenhum aparelho cadastrado.")
            for ap in lista_aparelhos:
                print(ap)
                
        elif opcao == '3':
            print("\n--- Cadastro de Exercicio ---")
            nome = input("Nome do Exercicio (ex: Supino Reto): ")
            grupo = input("Grupo Muscular (ex: Peitoral): ")
            
            exercicio = Exercicio(nome, grupo)
            lista_exercicios.append(exercicio)
            print(f"Sucesso: Exercicio '{exercicio.nome}' cadastrado!")
            
        elif opcao == '4':
            print("\n--- Exercicios Cadastrados ---")
            if not lista_exercicios:
                print("Nenhum exercicio cadastrado.")
            for ex in lista_exercicios:
                print(ex)
                
        elif opcao == '5':
            break
