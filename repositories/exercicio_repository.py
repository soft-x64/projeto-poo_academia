from database import get_connection

class ExercicioRepository:
    def inserir(self, exercicio_obj):
        sql = "INSERT INTO exercicio (nome, grupo_muscular) VALUES (%s, %s) RETURNING id;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (exercicio_obj.nome, exercicio_obj.grupo_muscular))
            id_inserido = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return id_inserido
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro ExercicioRepository.inserir]: {e}")
            raise e
        finally:
            if conn: conn.close()

    def listar_todos(self):
        sql = "SELECT id, nome, grupo_muscular FROM exercicio ORDER BY nome;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Exception as e:
            print(f"[Erro ExercicioRepository.listar_todos]: {e}")
            return []
        finally:
            if conn: conn.close()
