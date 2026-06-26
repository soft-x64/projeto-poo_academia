from datetime import date
from models.execeptions import ValorInvalidoError

class AvaliacaoFisica:
    def __init__(self, aluno, instrutor, data: date, percentual_gordura: float, observacoes: str = "", id_avaliacao=None):
        self._aluno = aluno
        self._instrutor = instrutor  # Vincula o instrutor/personal que fez a avaliação
        self._data = data
        self.percentual_gordura = percentual_gordura  # Dispara o setter para validar
        self._observacoes = observacoes
        self.id_avaliacao = id_avaliacao  # Mapeamento da PK do banco
    
    @property
    def aluno(self):
        return self._aluno

    @property
    def instrutor(self):
        return self._instrutor

    @property
    def data(self):
        return self._data

    @property
    def observacoes(self):
        return self._observacoes

    @property
    def percentual_gordura(self):
        return self._percentual_gordura

    @percentual_gordura.setter
    def percentual_gordura(self, valor):
        if not (0 < valor < 100):
             raise ValorInvalidoError("Percentual de gordura deve estar entre 0 e 100")
        self._percentual_gordura = valor

    def __str__(self):
        return f"Avaliação de {self._aluno.nome} por {self._instrutor.nome} em {self._data}: {self.percentual_gordura}% gordura"
