from models.pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, nome, cpf, email, telefone, cref: str, especialidade: str, id_instrutor=None):
        # Passa os dados comuns para a classe mãe (Pessoa)
        super().__init__(nome, cpf, email, telefone)
        
        # Guarda o ID do banco de dados
        self.id_instrutor = id_instrutor
        
        # Define os atributos privados correspondentes às properties
        self._cref = cref
        self._especialidade = especialidade
    
    @property
    def cref(self):
        return self._cref
    
    @property
    def especialidade(self):
        return self._especialidade
    
    def exibir_perfil(self) -> str:
        # Polimorfismo: formato diferente do Aluno
        return f"[INSTRUTOR] {self.nome} | CREF: {self.cref} | Especialidade: {self.especialidade}"
    
    def __str__(self):
        return self.exibir_perfil()
