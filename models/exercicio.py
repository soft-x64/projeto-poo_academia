class Exercicio:
    def __init__(self, nome, grupo_muscular, id=None):
        self._id = id
        self._nome = nome
        self._grupo_muscular = grupo_muscular

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def grupo_muscular(self):
        return self._grupo_muscular
