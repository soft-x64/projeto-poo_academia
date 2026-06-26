from datetime import date
from models.avaliacao_fisica import AvaliacaoFisica
from models.execeptions import ValorInvalidoError

def menu_avaliacoes(lista_alunos, lista_avaliacoes):
    while True:
        print("\n--- GESTAO DE AVALIACOES FISICAS ---")
        print("1. Registrar Avaliacao Fisica")
        print("2. Consultar Avaliacoes de um Aluno")
        print("3. Voltar")
        
        opcao = input("Escolha uma opcao: ")
        if opcao == '1':
            print("\n--- Registrar Avaliacao ---")
            cpf_aluno = input("Digite o CPF do Aluno: ")
            
            aluno = None
            for a in lista_alunos:
                if a.cpf == cpf_aluno:
                    aluno = a
                    break
            
            if not aluno:
                print("Erro: Aluno nao encontrado! Cadastre o aluno primeiro.")
                continue
                
            try:
                perc_gordura = float(input("Percentual de Gordura (%): "))
                obs = input("Observacoes (opcional): ")
                
                av = AvaliacaoFisica(aluno, date.today(), perc_gordura, obs)
                lista_avaliacoes.append(av)
                print(f"Sucesso: Avaliacao registrada para {aluno.nome}!")
            except ValorInvalidoError as e:
                print(f"Erro de validacao: {e}")
            except ValueError:
                print("Erro: Insira um valor numerico valido.")
                
        elif opcao == '2':
            print("\n--- Consulta de Avaliacoes ---")
            cpf_aluno = input("Digite o CPF do Aluno para consulta: ")
            
            aluno_existe = any(a.cpf == cpf_aluno for a in lista_alunos)
            if not aluno_existe:
                print("Erro: Aluno nao encontrado.")
                continue
                
            encontrou = False
            for av in lista_avaliacoes:
                if av._aluno.cpf == cpf_aluno:
                    print(av)
                    encontrou = True
            if not encontrou:
                print("Nenhuma avaliacao registrada para este aluno.")
                
        elif opcao == '3':
            break
