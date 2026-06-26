from database.connection import get_connection

class AlunoRepository:
    def __init__(self):
        pass

    def inserir(self, aluno_obj):
        """Recebe um objeto Aluno e insere no banco."""
        sql = """
            INSERT INTO aluno (nome, cpf, email, telefone) 
            VALUES (%s, %s, %s, %s) RETURNING id;
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            # Possu ajustar os atributos, tipo nome, cpf e etc, conforme a classe criada por nós
            cursor.execute(sql, (aluno_obj.nome, aluno_obj.cpf, aluno_obj.email, aluno_obj.telefone))
            id_inserido = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return id_inserido
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro AlunoRepository.inserir]: {e}")
            raise e
        finally:
            if conn: conn.close()

    def listar_todos(self):
        """Retorna todos os alunos cadastrados."""
        sql = "SELECT id, nome, cpf, email, telefone FROM aluno ORDER BY nome;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados  # Retorna uma lista de tuplas
        except Exception as e:
            print(f"[Erro AlunoRepository.listar_todos]: {e}")
            return []
        finally:
            if conn: conn.close()

    def buscar_por_id(self, id_aluno):
        """Busca um aluno específico pelo seu ID."""
        sql = "SELECT id, nome, cpf, email, telefone FROM aluno WHERE id = %s;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (id_aluno,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Exception as e:
            print(f"[Erro AlunoRepository.buscar_por_id]: {e}")
            return None
        finally:
            if conn: conn.close()

    def buscar_por_cpf(self, cpf):
        """Busca um aluno pelo CPF (Útil para a regra de negócio de não duplicar)."""
        sql = "SELECT id, nome, cpf, email, telefone FROM aluno WHERE cpf = %s;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (cpf,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado
        except Exception as e:
            print(f"[Erro AlunoRepository.buscar_por_cpf]: {e}")
            return None
        finally:
            if conn: conn.close()

    def atualizar(self, id_aluno, aluno_obj):
        """Atualiza os dados de um aluno existente."""
        sql = """
            UPDATE aluno 
            SET nome = %s, cpf = %s, email = %s, telefone = %s 
            WHERE id = %s;
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (aluno_obj.nome, aluno_obj.cpf, aluno_obj.email, aluno_obj.telefone, id_aluno))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro AlunoRepository.atualizar]: {e}")
            return False
        finally:
            if conn: conn.close()

    def excluir(self, id_aluno):
        """Remove um aluno do banco de dados pelo ID."""
        sql = "DELETE FROM aluno WHERE id = %s;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (id_aluno,))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro AlunoRepository.excluir]: {e}")
            return False
        finally:
            if conn: conn.close()
