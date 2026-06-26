# services/aluno_service.py
from models.aluno import Aluno

class AlunoService:
    def __init__(self, aluno_repository):
        """Recebe o AlunoRepository desenvolvido pelo Eduardo."""
        self.aluno_repo = aluno_repository

    def cadastrar_aluno(self, aluno_obj):
        
        registro_banco = self.aluno_repo.buscar_por_cpf(aluno_obj.cpf)
        
        if registro_banco is not None:
   
            raise Exception(f"Regra de Negócio: O CPF {aluno_obj.cpf} já está cadastrado no banco de dados!")
            
      
        self.aluno_repo.inserir(aluno_obj)

    def listar_alunos(self):
        """Retorna os alunos convertidos de tuplas do banco para objetos da classe Aluno."""
        linhas_banco = self.aluno_repo.listar_todos()
        lista_objetos = []
        
        for linha in linhas_banco:
            
            aluno_obj = Aluno(linha[1], linha[2], linha[3], linha[4], 0.0, 0.0)
            lista_objetos.append(aluno_obj)
            
        return lista_objetos
