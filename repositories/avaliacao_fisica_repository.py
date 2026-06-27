from database import get_connection

class AvaliacaoFisicaRepository:
    def inserir(self, avaliacao_obj):
        sql = """
            INSERT INTO avaliacao_fisica (aluno_id, peso, altura, data_avaliacao) 
            VALUES (%s, %s, %s, %s) RETURNING id;
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (
                avaliacao_obj.aluno_id, 
                avaliacao_obj.peso, 
                avaliacao_obj.altura, 
                avaliacao_obj.data_avaliacao
            ))
            id_inserido = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return id_inserido
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro AvaliacaoFisicaRepository.inserir]: {e}")
            raise e
        finally:
            if conn: conn.close()

    def listar_por_aluno(self, aluno_id):
        sql = "SELECT id, peso, altura, data_avaliacao FROM avaliacao_fisica WHERE aluno_id = %s ORDER BY data_avaliacao DESC;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (aluno_id,))
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Exception as e:
            print(f"[Erro AvaliacaoFisicaRepository.listar_por_aluno]: {e}")
            return []
        finally:
            if conn: conn.close()
