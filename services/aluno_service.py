class AlunoService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, aluno):
        # O service recebe o objeto pronto e repassa para o repository
        self.repository.salvar(aluno)

    def listar_todos(self):
        return self.repository.listar()

    def excluir(self, aluno_id):
        sucesso = self.repository.excluir(aluno_id)
        if sucesso:
            print("Aluno excluído com sucesso!")
        else:
            print(f"Erro: Nenhum aluno encontrado com o ID {aluno_id}.")
