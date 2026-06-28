import psycopg2
from models.ficha_treino import FichaTreino

class FichaTreinoRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, ficha):
        cursor = self.conn.cursor()
        try:
            sql = "INSERT INTO ficha_treino (idaluno, datainicio, datavencimento) VALUES (%s, %s, %s) RETURNING id"
            cursor.execute(sql, (ficha.idAluno, ficha.dataInicio, ficha.dataVencimento))
            id_ficha = cursor.fetchone()[0]
            self.conn.commit()
            return id_ficha
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()

    def listar_todos(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT id, idaluno, datainicio, datavencimento FROM ficha_treino")
            return cursor.fetchall()
        finally:
            cursor.close()
