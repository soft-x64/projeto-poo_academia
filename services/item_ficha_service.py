class ItemFichaService:
    def __init__(self, repository):
        self.repository = repository

    def adicionar(self, id_ficha, id_ex, s, r, c):
        from models.item_ficha_treino import ItemFichaTreino
        item = ItemFichaTreino(idFicha=id_ficha, idExercicio=id_ex, series=s, repeticoes=r, cargas=c)
        self.repository.salvar(item)

    def listar_da_ficha(self, id_ficha):
        return self.repository.listar_da_ficha(id_ficha)
