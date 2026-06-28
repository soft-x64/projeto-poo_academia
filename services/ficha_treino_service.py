class FichaTreinoService:
    def __init__(self, repository):
        self.repository = repository

    def criar(self, ficha):
        self.repository.salvar(ficha)

    def listar_todas(self):
        # O método no repository chama-se listar()
        return self.repository.listar()

    def excluir(self, ficha_id):
        if self.repository.excluir(ficha_id):
            print("Ficha excluída com sucesso!")
        else:
            print(f"Erro: Ficha {ficha_id} não encontrada.")
