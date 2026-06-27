from database import get_connection

class AparelhoRepository:
    def inserir(self, aparelho_obj):
        sql = "INSERT INTO aparelho (nome, tipo) VALUES (%s, %s) RETURNING id;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (aparelho_obj.nome, aparelho_obj.tipo))
            id_inserido = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return id_inserido
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro AparelhoRepository.inserir]: {e}")
            raise e
        finally:
            if conn: conn.close()

    def listar_todos(self):
        sql = "SELECT id, nome, tipo FROM aparelho ORDER BY nome;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Exception as e:
            print(f"[Erro AparelhoRepository.listar_todos]: {e}")
            return []
        finally:
            if conn: conn.close()
