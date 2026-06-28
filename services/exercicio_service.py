class ExercicioService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, exercicio):
        # Agora ele recebe apenas o objeto, como definido no seu menu
        self.repository.salvar(exercicio)

    def listar_todos(self):
        return self.repository.listar()

    def excluir(self, exercicio_id):
        self.repository.excluir(exercicio_id)
        print("Exercício excluído com sucesso!")
