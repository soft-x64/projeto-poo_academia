from database import get_connection

class AlunoRepository:
    def inserir(self, aluno_obj):
        sql = "INSERT INTO aluno (nome, cpf, email, telefone) VALUES (%s, %s, %s, %s) RETURNING id;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
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

    def atualizar(self, aluno_obj):
        sql = "UPDATE aluno SET nome = %s, email = %s, telefone = %s WHERE id = %s;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (aluno_obj.nome, aluno_obj.email, aluno_obj.telefone, aluno_obj.id))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            if conn: conn.rollback()
            print(f"Erro ao atualizar: {e}")
            return False
        finally:
            if conn: conn.close()

    def buscar_por_cpf(self, cpf):
        sql = "SELECT id FROM aluno WHERE cpf = %s;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (cpf,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado is not None
        except Exception as e:
            print(f"[Erro AlunoRepository.buscar_por_cpf]: {e}")
            return False
        finally:
            if conn: conn.close()

    def listar_todos(self):
        sql = "SELECT id, nome, cpf, email, telefone FROM aluno ORDER BY nome;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Exception as e:
            print(f"[Erro AlunoRepository.listar_todos]: {e}")
            return []
        finally:
            if conn: conn.close()

    def excluir(self, id_aluno):
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
