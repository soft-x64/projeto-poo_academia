from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, email, telefone):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._telefone = telefone

    @abstractmethod
    def exibir_perfil(self):
        pass
