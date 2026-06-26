class Aparelho:
    def __init__(self, nome: str, tipo: str, capacidade_carga: float = None, id_aparelho=None):
        # Guardamos com o underscore (_) para bater com as propriedades privadas
        self._nome = nome
        self._tipo = tipo 
        self.capacidade_carga = capacidade_carga
        self.id_aparelho = id_aparelho # Mapeamento da PK do banco
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def tipo(self):
        return self._tipo
    
    def __str__(self):
        capacidade = f" | Carga Máx: {self.capacidade_carga}kg" if self.capacidade_carga else ""
        return f"{self.nome} ({self.tipo}){capacidade}"
