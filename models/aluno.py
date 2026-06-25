from models.pessoa import Pessoa
from models.execeptions import ValorInvalidoError

class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, telefone, peso: float, altura: float):
        super().__init__(nome, cpf, email,telefone)
        self.peso = peso
        self.altura = altura
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("Peso deve ser maior que zero")
        self._peso = valor

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("Altura deve ser maior que zero")
        self._altura = valor
    
    def exibir_perfil(self) -> str:
        return f"[ALUNO] {self.nome} | Peso: {self.peso}kg | Altura: {self.altura}m"
    
    def __str__(self):
        return self.exibir_perfil()