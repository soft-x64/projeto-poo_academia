from database import get_connection

# Importando os Repositories
from repositories.aluno_repository import AlunoRepository
from repositories.instrutor_repository import InstrutorRepository
from repositories.aparelho_repository import AparelhoRepository
from repositories.exercicio_repository import ExercicioRepository
from repositories.ficha_treino_repository import FichaTreinoRepository
from repositories.avaliacao_fisica_repository import AvaliacaoFisicaRepository

# Importando os Services
from services.aluno_service import AlunoService
from services.instrutor_service import InstrutorService
from services.aparelho_service import AparelhoService
from services.exercicio_service import ExercicioService
from services.ficha_treino_service import FichaTreinoService
from services.avaliacao_fisica_service import AvaliacaoFisicaService

# Importando a função do menu
from ui.menu_principal import exibir_menu_principal

def main():
    # Instanciando Repositories
    aluno_repo = AlunoRepository()
    instrutor_repo = InstrutorRepository()
    aparelho_repo = AparelhoRepository()
    exercicio_repo = ExercicioRepository()
    ficha_repo = FichaTreinoRepository()
    avaliacao_repo = AvaliacaoFisicaRepository()

    # Instanciando Services (Injeção de Dependência)
    aluno_service = AlunoService(aluno_repo)
    instrutor_service = InstrutorService(instrutor_repo)
    aparelho_service = AparelhoService(aparelho_repo)
    exercicio_service = ExercicioService(exercicio_repo)
    ficha_service = FichaTreinoService(ficha_repo)
    avaliacao_service = AvaliacaoFisicaService(avaliacao_repo)

    # Executa o menu passando todos os serviços necessários
    exibir_menu_principal(
        aluno_service, 
        instrutor_service, 
        aparelho_service, 
        exercicio_service, 
        ficha_service, 
        avaliacao_service
    )

if __name__ == "__main__":
    main()
