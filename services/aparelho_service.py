class AparelhoService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, aparelho):
        # O Service apenas encaminha o objeto para o Repository
        self.repository.salvar(aparelho)

    def listar_todos(self):
        return self.repository.listar()

    def excluir(self, aparelho_id):
        if self.repository.excluir(aparelho_id):
            print("Aparelho excluído com sucesso!")
        else:
            print(f"Erro: Nenhum aparelho encontrado com o ID {aparelho_id}.")
