from models.pessoa import Pessoa

class Personal(Pessoa):
    def __init__(self, nome, cpf, email, telefone, cref: str, especialidade: str):
        super().__init__(nome, cpf, email, telefone)
        self.cref = cref
        self.especialidade = especialidade
    
    @property
    def cref(self):
        return self._cref
    
    @property
    def especialidade(self):
        return self._especialidade
    
    def exibir_perfil(self) -> str:
        return f"[PERSONAL]: {self.nome} | CREF: {self.cref} | Especialidade: {self.especialidade}"
    
    def __str__(self):
        return self.exibir_perfil()