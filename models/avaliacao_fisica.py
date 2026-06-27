class AvaliacaoFisica:
    def __init__(self, aluno_id, peso, altura, data_avaliacao, id=None):
        self._id = id
        self._aluno_id = aluno_id
        self._peso = peso
        self._altura = altura
        self._data_avaliacao = data_avaliacao

    @property
    def id(self):
        return self._id

    @property
    def aluno_id(self):
        return self._aluno_id

    @property
    def peso(self):
        return self._peso

    @property
    def altura(self):
        return self._altura

    @property
    def data_avaliacao(self):
        return self._data_avaliacao
