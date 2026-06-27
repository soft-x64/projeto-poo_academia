class TreinoService:
    def __init__(self, repository):
        self.repository = repository

    def criar_ficha(self, id_aluno, id_instrutor, objetivo):
        # Regra de negócio: garantir que objetivo não seja vazio
        if not objetivo:
            raise ValueError("O objetivo do treino é obrigatório.")
        return self.repository.inserir_ficha(id_aluno, id_instrutor, objetivo)

    def adicionar_exercicio(self, id_ficha, id_exercicio, series, reps, carga):
        return self.repository.vincular_exercicio_a_ficha(id_ficha, id_exercicio, series, reps, carga)
    
