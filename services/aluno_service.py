class AlunoService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, aluno):
        self.repository.salvar(aluno)

    def listar_todos(self):
        return self.repository.listar()

    def excluir(self, aluno_id):
        # O repositório agora retorna True ou False
        sucesso = self.repository.excluir(aluno_id)
        if sucesso:
            print("Aluno excluído com sucesso!")
        else:
            print(f"Erro: Nenhum aluno encontrado com o ID {aluno_id}.")
