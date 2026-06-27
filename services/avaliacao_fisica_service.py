class AvaliacaoFisicaService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_avaliacao(self, avaliacao_obj):
        return self.repository.inserir(avaliacao_obj)

    def listar_avaliacoes_do_aluno(self, aluno_id):
        return self.repository.listar_por_aluno(aluno_id)
