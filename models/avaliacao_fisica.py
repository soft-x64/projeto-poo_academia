from datetime import date
from models.execeptions import ValorInvalidoError

class AvaliacaoFisica:
    def __init__(self, aluno, data: date, percentual_gordura: float, observacoes: str = ""):
        self._aluno = aluno
        self._data = data
        self.percentual_gordura = percentual_gordura
        self._observacoes = observacoes

    @property
    def percentual_gordura(self):
        return self._percentual_gordura

    @percentual_gordura.setter
    def percentual_gordura(self, valor):
        if not (0 < valor < 100):
             raise ValorInvalidoError("Percentual de gordura deve estar entre 0 e 100")
        self._percentual_gordura = valor

    def __str__(self):
        return f"Avaliação de {self._aluno.nome} em {self._data}: {self.percentual_gordura}% gordura"
