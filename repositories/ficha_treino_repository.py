from database import get_connection

class FichaTreinoRepository:
    def inserir(self, ficha_obj):
        sql = "INSERT INTO ficha_treino (aluno_id, instrutor_id, descricao) VALUES (%s, %s, %s) RETURNING id;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (ficha_obj.aluno_id, ficha_obj.instrutor_id, ficha_obj.descricao))
            id_inserido = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return id_inserido
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro FichaTreinoRepository.inserir]: {e}")
            raise e
        finally:
            if conn: conn.close()

    def listar_todos(self):
        # Join para trazer nomes e facilitar a visualização
        sql = """
            SELECT f.id, a.nome, i.nome, f.descricao 
            FROM ficha_treino f
            JOIN aluno a ON f.aluno_id = a.id
            JOIN instrutor i ON f.instrutor_id = i.id;
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Exception as e:
            print(f"[Erro FichaTreinoRepository.listar_todos]: {e}")
            return []
        finally:
            if conn: conn.close()
