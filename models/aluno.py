from .pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, telefone, peso, id=None):
        super().__init__(nome, cpf, email, telefone)
        self._id = id  # ID necessário para operações de atualização e exclusão
        self._peso = peso

    def exibir_perfil(self):
        return f"[ALUNO] {self._nome} | Peso: {self._peso}kg"

    # Adicionei os getters caso precise acessar os valores protegidos fora da classe
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def email(self):
        return self._email

    @property
    def telefone(self):
        return self._telefone

    @property
    def peso(self):
        return self._peso
