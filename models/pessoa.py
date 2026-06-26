from models.execeptions import CPFInvalidoError
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, email: str, telefone: str):
        # Usamos os setters aqui (com self.nome em vez de self._nome) 
        # para garantir que as validações rodem logo no cadastro
        self.nome = nome
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
        # Remove pontos e traços caso o usuário digite com máscara
        cpf_limpo = valor.replace(".", "").replace("-", "") if valor else ""
        
        if not cpf_limpo or len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
            raise CPFInvalidoError(f"CPF inválido: {valor}")
        self._cpf = cpf_limpo
    
    @abstractmethod
    def exibir_perfil(self) -> str:
        pass

    def __str__(self):
        return f"{self.nome} (CPF: {self._cpf})"
    
