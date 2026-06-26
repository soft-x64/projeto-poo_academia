# services/aluno_service.py

class AlunoService:
    def __init__(self, aluno_repository):
        # Aqui você recebe o mecanismo de banco de dados que o Eduardo vai fazer
        self.aluno_repo = aluno_repository

    def cadastrar_aluno(self, aluno):
        # REGRA DE NEGÓCIO: CHAMA O BANCO PARA VER SE O CPF JÁ EXISTE
        aluno_existente = self.aluno_repo.buscar_por_cpf(aluno.cpf)
        
        if aluno_existente:
            # Se o banco encontrar alguém com esse CPF, o sistema barra e joga o erro
            raise Exception(f"Regra de Negócio: O CPF {aluno.cpf} já está cadastrado!")
            
        # Se não encontrou ninguém, a regra permite passar e manda salvar no banco
        self.aluno_repo.salvar(aluno)

    def listar_alunos(self):
        return self.aluno_repo.listar_todos()
