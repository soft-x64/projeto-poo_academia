from datetime import datetime
from models.ficha_treino import FichaTreino

class FichaTreinoService:
    def __init__(self, repository):
        self.repository = repository

    def criar_ficha(self, id_aluno, data_inicio_str, data_venc_str):
        inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y").strftime("%Y-%m-%d")
        venc = datetime.strptime(data_venc_str, "%d/%m/%Y").strftime("%Y-%m-%d")
        return self.repository.salvar(FichaTreino(idAluno=id_aluno, dataInicio=inicio, dataVencimento=venc))

    def listar_todas(self):
        return self.repository.listar_todos()

    def excluir(self, id_ficha):
        return self.repository.excluir(id_ficha)
