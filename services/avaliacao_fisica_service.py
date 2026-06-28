from datetime import datetime

class AvaliacaoFisicaService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar(self, avaliacao):
        try:
            if avaliacao.data:
                # Converte para formato SQL AAAA-MM-DD
                data_formatada = datetime.strptime(avaliacao.data, "%d/%m/%Y").strftime("%Y-%m-%d")
                avaliacao.data = data_formatada
            self.repository.salvar(avaliacao)
            print("Avaliação cadastrada com sucesso!")
        except ValueError:
            print("Erro: Formato de data inválido. Use DD/MM/AAAA.")
        except Exception as e:
            print(f"Erro ao salvar: {e}")

    def listar_por_aluno(self, id_aluno):
        return self.repository.listar_por_aluno(id_aluno)

    def excluir(self, id_avaliacao):
        if self.repository.excluir(id_avaliacao):
            print("Avaliação excluída com sucesso!")
        else:
            print("Erro: Avaliação não encontrada.")
