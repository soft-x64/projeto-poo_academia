from database import get_connection

class InstrutorRepository:
    def inserir(self, instrutor_obj):
        sql = """
            INSERT INTO instrutor (nome, cpf, email, telefone, especialidade) 
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (
                instrutor_obj.nome, 
                instrutor_obj.cpf, 
                instrutor_obj.email, 
                instrutor_obj.telefone, 
                instrutor_obj.especialidade
            ))
            id_inserido = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            return id_inserido
        except Exception as e:
            if conn: conn.rollback()
            print(f"[Erro InstrutorRepository.inserir]: {e}")
            raise e
        finally:
            if conn: conn.close()

    def listar_todos(self):
        sql = "SELECT id, nome, cpf, email, telefone, especialidade FROM instrutor ORDER BY nome;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        except Exception as e:
            print(f"[Erro InstrutorRepository.listar_todos]: {e}")
            return []
        finally:
            if conn: conn.close()

    def buscar_por_cpf(self, cpf):
        sql = "SELECT id FROM instrutor WHERE cpf = %s;"
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (cpf,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado is not None
        except Exception as e:
            print(f"[Erro InstrutorRepository.buscar_por_cpf]: {e}")
            return False
        finally:
            if conn: conn.close()
