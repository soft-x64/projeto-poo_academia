from models.avaliacao_fisica import AvaliacaoFisica

class AvaliacaoFisicaService:
    def __init__(self, repository):
        self.repository = repository

    def registrar(self, alunoId, instrutorId, peso, altura):
        p = float(peso)
        a = float(altura)
        imc = p / (a * a)
        
        av = AvaliacaoFisica(alunoId=int(alunoId), instrutorId=int(instrutorId), peso=p, altura=a, imc=round(imc, 2))
        self.repository.salvar(av)

    def listar_do_aluno(self, alunoId):
        return self.repository.buscar_por_aluno(alunoId)
