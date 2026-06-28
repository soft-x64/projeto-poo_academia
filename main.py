# Importações de Repositories
from repositories.aluno_repository import AlunoRepository
from repositories.instrutor_repository import InstrutorRepository
from repositories.aparelho_repository import AparelhoRepository
from repositories.exercicio_repository import ExercicioRepository
from repositories.ficha_treino_repository import FichaTreinoRepository
from repositories.item_ficha_repository import ItemFichaRepository

# Importações de Services
from services.aluno_service import AlunoService
from services.instrutor_service import InstrutorService
from services.aparelho_service import AparelhoService
from services.exercicio_service import ExercicioService
from services.ficha_treino_service import FichaTreinoService
from services.item_ficha_service import ItemFichaService

# Importações de UI
from ui.menu_aluno import sub_menu_aluno
from ui.menu_instrutor import sub_menu_instrutor
from ui.menu_aparelho import sub_menu_aparelho
from ui.menu_exercicio import sub_menu_exercicio
from ui.menu_ficha import sub_menu_ficha

def main():
    # Inicializa Repositories
    aluno_repo = AlunoRepository()
    instrutor_repo = InstrutorRepository()
    aparelho_repo = AparelhoRepository()
    exercicio_repo = ExercicioRepository()
    ficha_repo = FichaTreinoRepository()
    item_repo = ItemFichaRepository()

    # Inicializa Services
    aluno_service = AlunoService(aluno_repo)
    instrutor_service = InstrutorService(instrutor_repo)
    aparelho_service = AparelhoService(aparelho_repo)
    exercicio_service = ExercicioService(exercicio_repo)
    ficha_service = FichaTreinoService(ficha_repo)
    item_service = ItemFichaService(item_repo)

    while True:
        print("\n" + "="*30)
        print("   SISTEMA DE ACADEMIA - POO")
        print("="*30)
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Instrutores")
        print("3. Gerenciar Aparelhos")
        print("4. Gerenciar Exercícios")
        print("5. Gerenciar Fichas de Treino")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            sub_menu_aluno(aluno_service)
        elif opcao == "2":
            sub_menu_instrutor(instrutor_service)
        elif opcao == "3":
            sub_menu_aparelho(aparelho_service)
        elif opcao == "4":
            # Passamos o aparelho_service aqui para que o menu exercicio possa listar aparelhos
            sub_menu_exercicio(exercicio_service, aparelho_service)
        elif opcao == "5":
            sub_menu_ficha(ficha_service, item_service, exercicio_service)
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("[!] Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
