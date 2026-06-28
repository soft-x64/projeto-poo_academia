class InstrutorService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, instrutor):
        self.repository.salvar(instrutor)

    def listar_todos(self):
        return self.repository.listar()

    def excluir(self, instrutor_id):
        # Verifica o resultado booleano vindo do repositório
        if self.repository.excluir(instrutor_id):
            print("Instrutor excluído com sucesso!")
        else:
            print(f"Erro: Nenhum instrutor encontrado com o ID {instrutor_id}.")
