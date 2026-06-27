class FichaTreino:
    def __init__(self, aluno_id, instrutor_id, descricao, id=None):
        self._id = id
        self._aluno_id = aluno_id
        self._instrutor_id = instrutor_id
        self._descricao = descricao

    @property
    def id(self):
        return self._id

    @property
    def aluno_id(self):
        return self._aluno_id

    @property
    def instrutor_id(self):
        return self._instrutor_id

    @property
    def descricao(self):
        return self._descricao
