import psycopg2
from models.aparelho import Aparelho

class AparelhoRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, aparelho):
        cursor = self.conn.cursor()
        # Coluna corrigida para 'grupomuscular'
        sql = "INSERT INTO aparelho (nome, grupomuscular) VALUES (%s, %s)"
        cursor.execute(sql, (aparelho.nome, aparelho.grupo_muscular))
        self.conn.commit()
        cursor.close()

    def listar(self):
        cursor = self.conn.cursor()
        # Coluna corrigida para 'grupomuscular'
        cursor.execute("SELECT id, nome, grupomuscular FROM aparelho")
        resultados = cursor.fetchall()
        cursor.close()
        return [Aparelho(id=r[0], nome=r[1], grupo_muscular=r[2]) for r in resultados]

    def excluir(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM aparelho WHERE id = %s", (id,))
            linhas = cursor.rowcount
            self.conn.commit()
            return linhas > 0
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao excluir: {e}")
            return False
        finally:
            cursor.close()
