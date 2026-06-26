from models.aluno import Aluno
from models.personal import Personal
from models.execeptions import CPFInvalidoError, ValorInvalidoError

def menu_usuarios(aluno_service, instrutor_repository):
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
                
                aluno_service.cadastrar_aluno(aluno)
                print(f"Sucesso: Aluno {aluno.nome} cadastrado com exito!")
                
            except (CPFInvalidoError, ValorInvalidoError) as e:
                print(f"Erro de Validacao: {e}")
            except ValueError:
                print("Erro: insira valores numericos validos.")
            except Exception as e:
             
                print(f"Erro no Cadastro: {e}")
                
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
                
                instrutor_repository.inserir(personal)
                print(f"Sucesso: Personal {personal.nome} cadastrado com exito!")
            except CPFInvalidoError as e:
                print(f"Erro: {e}")
            except ValueError:
                print("Erro: dados invalidos.")
            except Exception as e:
                print(f"Erro no Cadastro: {e}")
                
        elif opcao == '3':
            print("\n--- Todos os Usuarios Cadastrados (Banco de Dados) ---")
    
            lista_alunos = aluno_service.listar_alunos()
            
        
            lista_personais = []
            for linha in instrutor_repository.listar_todos():

                p = Personal(linha[1], linha[2], linha[3], linha[4], linha[5], "Geral")
                lista_personais.append(p)
                
            todos = lista_alunos + lista_personais
            if not todos:
                print("Nenhum usuario cadastrado no Banco de Dados.")
            for u in todos:
                print(u.exibir_perfil()) 
                
        elif opcao == '4':
            break