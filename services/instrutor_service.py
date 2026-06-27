class InstrutorService:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar_instrutor(self, instrutor_obj):
        # Verifica se o CPF já existe para evitar duplicidade (Regra de Negócio)
        if self.repository.buscar_por_cpf(instrutor_obj.cpf):
            print("Erro: CPF do instrutor já cadastrado!")
            return None
        return self.repository.inserir(instrutor_obj)

    def listar_instrutores(self):
        return self.repository.listar_todos()

    # Podemos adicionar outros métodos conforme a necessidade, 
    # como remover ou atualizar, seguindo o padrão que fizemos para Aluno.
