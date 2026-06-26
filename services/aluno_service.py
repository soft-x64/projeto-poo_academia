from models.aluno import Aluno
class AlunoService:
    def __init__(self, aluno_repository):
    
        self.aluno_repo = aluno_repository

    def cadastrar_aluno(self, aluno_obj: Aluno):
        
        registro_existente = self.aluno_repo.buscar_por_cpf(aluno_obj.cpf)
        
        if registro_existente:
       
            raise Exception(f"Regra de Negocio: O CPF '{aluno_obj.cpf}' ja esta cadastrado no sistema!")
        id_gerado = self.aluno_repo.inserir(aluno_obj)
        return id_gerado

    def listar_alunos(self):
        linhas = self.aluno_repo.listar_todos()
        alunos_objetos = []
        for linha in linhas:
            aluno = Aluno(linha[1], linha[2], linha[3], linha[4], 0.0, 0.0)
            alunos_objetos.append(aluno)
        return alunos_objetos