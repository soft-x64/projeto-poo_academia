from models.aparelho import Aparelho

class AparelhoService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, nome, grupo):
        novo = Aparelho(nome=nome, grupoMuscular=grupo)
        self.repository.salvar(novo)

    def listar_todos(self):
        return self.repository.listar()

    def excluir(self, id_aparelho):
        self.repository.excluir(id_aparelho)
