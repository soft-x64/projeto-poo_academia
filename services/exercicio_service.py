class ExercicioService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar_exercicio(self, exercicio_obj):
        return self.repository.inserir(exercicio_obj)

    def listar_exercicios(self):
        return self.repository.listar_todos()
