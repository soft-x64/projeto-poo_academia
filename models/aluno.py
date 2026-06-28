from models.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, id=None, nome=None, cpf=None, email=None, telefone=None, objetivo=None):
        super().__init__(nome, cpf, email, telefone)
        self.id = id
        self.objetivo = objetivo

    def exibir_perfil(self):
        return f"Aluno: {self._nome} | Objetivo: {self.objetivo}"
