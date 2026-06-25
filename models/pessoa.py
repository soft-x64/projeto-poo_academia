from models.execeptions import CPFInvalidoError
from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self,nome: str, cpf: str, email: str, telefone: str):
        self.nome= nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor if valor else ""

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, valor):
        if not valor or len(valor) != 11 or not valor.isdigit():
            raise CPFInvalidoError(f"CPF: invalido: `{valor}")
        self._cpf = valor
    
    @abstractmethod
    def exibir_perfil(self) -> str:
        pass

    def __str__(self):
        return f"`{self.nome} (CPF: `{self._cpf})"
    