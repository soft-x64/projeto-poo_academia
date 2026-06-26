from database.connection import get_connection

class TreinoRepository:
    def inserir_ficha(self, id_aluno, id_instrutor, objetivo):
        """Cria o cabeçalho da ficha de treino."""
        sql = """
            INSERT INTO ficha_treino (id_aluno, id_instrutor, objetivo) 
            VALUES (%s, %s, %s) RETURNING id;
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (id_aluno, id_instrutor, objetivo))
            id_ficha = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return id_ficha
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro TreinoRepository.inserir_ficha]: {e}")
            raise e
        finally:
            if conn: conn.close()

    def vincular_exercicio_a_ficha(self, id_ficha, id_exercicio, series, repeticoes, carga):
        """Adiciona os exercícios detalhados dentro da ficha criada."""
        sql = """
            INSERT INTO ficha_exercicio (id_ficha, id_exercicio, series, repeticoes, carga) 
            VALUES (%s, %s, %s, %s, %s);
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (id_ficha, id_exercicio, series, repeticoes, carga))
            conn.commit()
            cursor.close()
            return True
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro TreinoRepository.vincular_exercicio]: {e}")
            return False
        finally:
            if conn: conn.close()

    def buscar_fichas_por_aluno(self, id_aluno):
        """Lista todas as fichas associadas a um aluno específico."""
        sql = """
            SELECT ft.id, ft.data_criacao, ft.objetivo, inst.nome 
            FROM ficha_treino ft
            LEFT JOIN instrutor inst ON ft.id_instrutor = inst.id
            WHERE ft.id_aluno = %s ORDER BY ft.data_criacao DESC;
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (id_aluno,))
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Exception as e:
            print(f"[Erro TreinoRepository.buscar_fichas_por_aluno]: {e}")
            return []
        finally:
            if conn: conn.close()
