class AparelhoService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar_aparelho(self, aparelho_obj):
        return self.repository.inserir(aparelho_obj)

    def listar_aparelhos(self):
        return self.repository.listar_todos()
