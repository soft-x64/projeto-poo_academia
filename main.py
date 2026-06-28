from repositories.aluno_repository import AlunoRepository
from repositories.instrutor_repository import InstrutorRepository
from repositories.aparelho_repository import AparelhoRepository
from repositories.exercicio_repository import ExercicioRepository
from repositories.ficha_treino_repository import FichaTreinoRepository
from repositories.avaliacao_fisica_repository import AvaliacaoFisicaRepository

from services.aluno_service import AlunoService
from services.instrutor_service import InstrutorService
from services.aparelho_service import AparelhoService
from services.exercicio_service import ExercicioService
from services.ficha_treino_service import FichaTreinoService
from services.avaliacao_fisica_service import AvaliacaoFisicaService

from ui.menu_aluno import sub_menu_aluno
from ui.menu_instrutor import sub_menu_instrutor
from ui.menu_aparelho import sub_menu_aparelho
from ui.menu_exercicio import sub_menu_exercicio
from ui.menu_ficha import sub_menu_ficha
from ui.menu_avaliacao import sub_menu_avaliacao

def main():
    # Inicialização das instâncias
    aluno_service = AlunoService(AlunoRepository())
    instrutor_service = InstrutorService(InstrutorRepository())
    aparelho_service = AparelhoService(AparelhoRepository())
    exercicio_service = ExercicioService(ExercicioRepository())
    ficha_service = FichaTreinoService(FichaTreinoRepository())
    avaliacao_service = AvaliacaoFisicaService(AvaliacaoFisicaRepository())

    while True:
        print("\n==============================")
        print("   SISTEMA DE ACADEMIA - POO")
        print("==============================")
        print("1. Gerenciar Alunos")
        print("2. Gerenciar Instrutores")
        print("3. Gerenciar Aparelhos")
        print("4. Gerenciar Exercícios")
        print("5. Gerenciar Fichas de Treino")
        print("6. Gerenciar Avaliações Físicas")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sub_menu_aluno(aluno_service)
        elif opcao == "2":
            sub_menu_instrutor(instrutor_service)
        elif opcao == "3":
            sub_menu_aparelho(aparelho_service)
        elif opcao == "4":
            sub_menu_exercicio(exercicio_service, aparelho_service)
        elif opcao == "5":
            sub_menu_ficha(ficha_service, None, exercicio_service)
        elif opcao == "6":
            sub_menu_avaliacao(avaliacao_service)
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
