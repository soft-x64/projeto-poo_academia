class FichaTreinoService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar_ficha(self, ficha_obj, lista_exercicios):
        """
        Cadastra uma ficha de treino.
        Regra de negócio: A ficha deve conter pelo menos um exercício.
        """
        if not lista_exercicios or len(lista_exercicios) == 0:
            print("Erro: A ficha de treino deve conter pelo menos um exercício!")
            return None
            
        return self.repository.inserir(ficha_obj)

    def listar_fichas(self):
        return self.repository.listar_todos()
