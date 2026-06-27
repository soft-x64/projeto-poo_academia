class AlunoService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar_aluno(self, aluno_obj):
        if self.repository.buscar_por_cpf(aluno_obj.cpf):
            print("Erro: CPF já cadastrado!")
            return None
        return self.repository.inserir(aluno_obj)

    def atualizar_aluno(self, aluno_obj):
        return self.repository.atualizar(aluno_obj)

    def listar_alunos(self):
        return self.repository.listar_todos()

    def remover_aluno(self, id_aluno):
        return self.repository.excluir(id_aluno)
