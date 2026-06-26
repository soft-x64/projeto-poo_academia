class Aparelho:
    def __init__(self, nome: str, tipo: str, capacidade_carga: float = None):
        self.nome = nome
        self.tipo = tipo 
        self.capacidade_carga = capacidade_carga
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def tipo(self):
        return self._tipo
    
    def __str__(self):
        return f"{self.nome} ({self.tipo})"
    
