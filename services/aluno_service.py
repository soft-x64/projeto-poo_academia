# services/aluno_service.py

class AlunoService:
    def __init__(self, aluno_repository):
      
        self.aluno_repo = aluno_repository

    def cadastrar_aluno(self, aluno):
    
        aluno_existente = self.aluno_repo.buscar_por_cpf(aluno.cpf)
        
        if aluno_existente:
           
            raise Exception(f"Regra de Negócio: O CPF {aluno.cpf} já está cadastrado!")
            
 
        self.aluno_repo.salvar(aluno)

    def listar_alunos(self):
        return self.aluno_repo.listar_todos()
