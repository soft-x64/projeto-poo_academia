from .pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, nome, cpf, email, telefone, especialidade, id=None):
        # Chama o construtor da classe base Pessoa
        super().__init__(nome, cpf, email, telefone)
        self._id = id
        self._especialidade = especialidade

    def exibir_perfil(self):
        return f"[INSTRUTOR] {self._nome} | Especialidade: {self._especialidade}"

    # Getters para acesso via @property (mesmo padrão do Aluno)
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
    def especialidade(self):
        return self._especialidade
