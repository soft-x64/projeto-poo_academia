from repositories import AlunoRepository, InstrutorRepository, AparelhoRepository, ExercicioRepository, FichaTreinoRepository, AvaliacaoFisicaRepository
from services import AlunoService, InstrutorService, AparelhoService, ExercicioService, FichaTreinoService, AvaliacaoFisicaService
from ui import exibir_menu_principal

def main():
    # 1. Instanciamento dos Repositórios (conectam ao banco)
    aluno_repo = AlunoRepository()
    instrutor_repo = InstrutorRepository()
    aparelho_repo = AparelhoRepository()
    exercicio_repo = ExercicioRepository()
    ficha_repo = FichaTreinoRepository()
    avaliacao_repo = AvaliacaoFisicaRepository()

    # 2. Instanciamento dos Services (regras de negócio)
    aluno_service = AlunoService(aluno_repo)
    instrutor_service = InstrutorService(instrutor_repo)
    aparelho_service = AparelhoService(aparelho_repo)
    exercicio_service = ExercicioService(exercicio_repo)
    ficha_service = FichaTreinoService(ficha_repo)
    avaliacao_service = AvaliacaoFisicaService(avaliacao_repo)

    # 3. Execução do Menu (Injeção de Dependência)
    # Aqui passamos todos os serviços que a UI precisa para funcionar
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
