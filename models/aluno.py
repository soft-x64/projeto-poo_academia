from models.pessoa import Pessoa
from models.execeptions import ValorInvalidoError

class Aluno(Pessoa):
    def __init__(self, nome, cpf, email, telefone, peso: float, altura: float, id_aluno=None):
        # Passa os dados comuns para a classe mãe (Pessoa)
        super().__init__(nome, cpf, email, telefone)
        
        # Guarda o ID do banco de dados (padrão é None para novos cadastros)
        self.id_aluno = id_aluno
        
        # Ativa as propriedades/setters para validar peso e altura
        self.peso = peso
        self.altura = altura
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("O peso deve ser maior que zero")
        self._peso = valor

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValorInvalidoError("A altura deve ser maior que zero")
        self._altura = valor
    
    def exibir_perfil(self) -> str:
        # Polimorfismo: implementa o método abstrato de Pessoa
        return f"[ALUNO] {self.nome} | Peso: {self.peso}kg | Altura: {self.altura}m"
    
    def __str__(self):
        return self.exibir_perfil()
