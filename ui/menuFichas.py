from models.ficha_treino import ItemFicha, FichaTreino
from models.execeptions import FichaSemExercicioError

def menu_fichas(lista_alunos, lista_personais, lista_exercicios, lista_fichas):
    while True:
        print("\n--- GESTAO DE FICHAS DE TREINO ---")
        print("1. Montar Nova Ficha de Treino")
        print("2. Consultar Ficha de um Aluno")
        print("3. Voltar")
        
        opcao = input("Escolha uma opcao: ")
        if opcao == '1':
            print("\n--- Montar Ficha de Treino ---")
            cpf_aluno = input("CPF do Aluno: ")
            aluno = None
            for a in lista_alunos:
                if a.cpf == cpf_aluno:
                    aluno = a
                    break
                    
            cpf_personal = input("CPF do Personal (Instrutor): ")
            personal = None
            for p in lista_personais:
                if p.cpf == cpf_personal:
                    personal = p
                    break
            
            if not aluno or not personal:
                print("Erro: Aluno ou Personal nao encontrado(s). Verifique os cadastros.")
                continue
                
            if not lista_exercicios:
                print("Erro: Nao ha exercicios cadastrados para montar a ficha! Va ao menu de Equipamentos.")
                continue
            
            nova_ficha = FichaTreino(aluno, personal)
            
            while True:
                print("\n--- Selecione o Exercicio ---")
                for i, ex in enumerate(lista_exercicios):
                    print(f"{i} - {ex.nome} ({ex.grupo_muscular})")
                
                escolha = input("Escolha o numero do exercicio (ou 'F' para finalizar a ficha): ")
                if escolha.upper() == 'F':
                    break
                    
                try:
                    idx = int(escolha)
                    exercicio_escolhido = lista_exercicios[idx]
                    
                    series = int(input("Quantidade de series: "))
                    repeticoes = int(input("Quantidade de repeticoes: "))
                    carga = float(input("Carga (kg): "))
                    
                    item = ItemFicha(exercicio_escolhido, series, repeticoes, carga)
                    nova_ficha.adicionar_item(item)
                    print(f"Adicionado: {exercicio_escolhido.nome} a ficha.")
                except (IndexError, ValueError):
                    print("Erro: Entrada invalida. Tente novamente.")
            
            try:
                nova_ficha.finalizar()
                lista_fichas.append(nova_ficha)
                print(f"Sucesso: Ficha de treino de {aluno.nome} criada!")
            except FichaSemExercicioError as e:
                print(f"Erro ao salvar ficha: {e}")
                
        elif opcao == '2':
            print("\n--- Consulta de Ficha ---")
            cpf_aluno = input("Digite o CPF do Aluno para buscar a ficha: ")
            
            encontrou = False
            for ficha in lista_fichas:
                aluno_ficha = getattr(ficha, 'aluno', getattr(ficha, '_aluno', None))
                if aluno_ficha and aluno_ficha.cpf == cpf_aluno:
                    print("-" * 30)
                    print(ficha)
                    encontrou = True
            if not encontrou:
                print("Nenhuma ficha de treino encontrada para este aluno.")
                
        elif opcao == '3':
            break
