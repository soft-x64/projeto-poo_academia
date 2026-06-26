class Exercicio:
    def __init__(self, nome: str, grupo_muscular: str, id_exercicio=None):
        # Guardamos com o underscore (_) para casar com as propriedades privadas
        self._nome = nome
        self._grupo_muscular = grupo_muscular
        self.id_exercicio = id_exercicio # Mapeamento da PK do banco
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def grupo_muscular(self):
        return self._grupo_muscular
    
    def __str__(self):
        return f"{self.nome} ({self.grupo_muscular})"
    
    
