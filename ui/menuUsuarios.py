from models.aluno import Aluno
from models.personal import Personal
from models.execeptions import CPFInvalidoError, ValorInvalidoError

def menu_usuarios(lista_alunos, lista_personais):
    while True:
        print("\n--- GESTAO DE USUARIOS ---")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Personal")
        print("3. Listar Todos (Polimorfismo)")
        print("4. Voltar")
        
        opcao = input("Escolha uma opcao: ")
        if opcao == '1':
            print("\n--- Cadastro de Aluno ---")
            try:
                nome = input("Nome: ")
                cpf = input("CPF (11 digitos): ")
                email = input("E-mail: ")
                telefone = input("Telefone: ")
                peso = float(input("Peso (kg): "))
                altura = float(input("Altura (m): "))
                
                aluno = Aluno(nome, cpf, email, telefone, peso, altura)
                lista_alunos.append(aluno)
                print(f"Sucesso: Aluno {aluno.nome} cadastrado!")
            except (CPFInvalidoError, ValorInvalidoError) as e:
                print(f"Erro: {e}")
            except ValueError:
                print("Erro: insira valores numericos validos.")
                
        elif opcao == '2':
            print("\n--- Cadastro de Personal ---")
            try:
                nome = input("Nome: ")
                cpf = input("CPF (11 digitos): ")
                email = input("E-mail: ")
                telefone = input("Telefone: ")
                cref = input("CREF: ")
                especialidade = input("Especialidade: ")
                
                personal = Personal(nome, cpf, email, telefone, cref, especialidade)
                lista_personais.append(personal)
                print(f"Sucesso: Personal {personal.nome} cadastrado!")
            except CPFInvalidoError as e:
                print(f"Erro: {e}")
            except ValueError:
                print("Erro: dados invalidos.")
                
        elif opcao == '3':
            print("\n--- Todos os Usuarios Cadastrados ---")
            todos = lista_alunos + lista_personais
            if not todos:
                print("Nenhum usuario cadastrado.")
            for u in todos:
                print(u.exibir_perfil()) # Executa o comportamento polimorfico
                
        elif opcao == '4':
            break
