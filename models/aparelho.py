class Aparelho:
    def __init__(self, nome, tipo, id=None):
        self._id = id
        self._nome = nome
        self._tipo = tipo

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo
