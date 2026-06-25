class Exercicio:
    def __init__(self, nome: str, grupo_muscular: str):
        self.nome = nome
        self.grupo_muscular = grupo_muscular
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def grupo_muscular(self):
        return self._grupo_muscular
    
    def __str__(self):
        return f"{self.nome} ({self.grupo_muscular})"
    
    