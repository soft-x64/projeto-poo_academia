from models.aluno import Aluno
from models.personal import Personal
from models.execeptions import CPFInvalidoError, ValorInvalidoError

# Mudamos os parâmetros para receber as camadas de banco/serviço
def menu_usuarios(aluno_service, personal_repository):
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
                
                # --- AQUI ENTRA A SUA REGRA DE NEGÓCIO ---
                aluno_service.cadastrar_aluno(aluno)
                print(f"Sucesso: Aluno {aluno.nome} cadastrado!")
                
            except (CPFInvalidoError, ValorInvalidoError) as e:
                print(f"Erro de Validação: {e}")
            except ValueError:
                print("Erro: insira valores numericos validos.")
            except Exception as e:
                # Captura o erro se o CPF for duplicado na regra de negócio
                print(f"Erro de Sistema: {e}")
                
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
                
                # Salva o personal no banco usando o repositório do Eduardo
                personal_repository.salvar(personal)
                print(f"Sucesso: Personal {personal.nome} cadastrado!")
            except CPFInvalidoError as e:
                print(f"Erro: {e}")
            except ValueError:
                print("Erro: dados invalidos.")
            except Exception as e:
                print(f"Erro de Sistema: {e}")
                
        elif opcao == '3':
            print("\n--- Todos os Usuarios Cadastrados ---")
            # Busca os dados atualizados vindos do banco de dados
            lista_alunos = aluno_service.listar_alunos()
            lista_personais = personal_repository.listar_todos()
            
            todos = lista_alunos + lista_personais
            if not todos:
                print("Nenhum usuario cadastrado.")
            for u in todos:
                print(u.exibir_perfil()) # Executa o comportamento polimorfico
                
        elif opcao == '4':
            break