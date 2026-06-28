from models.pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, id=None, nome=None, cpf=None, email=None, telefone=None, especialidade=None):
        super().__init__(nome, cpf, email, telefone)
        self.id = id
        self.especialidade = especialidade

    def exibir_perfil(self):
        return f"Instrutor: {self._nome} | Especialidade: {self.especialidade}"
