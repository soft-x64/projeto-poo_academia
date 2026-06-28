import psycopg2
from models.ficha_treino import FichaTreino

class FichaTreinoRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, ficha):
        cursor = self.conn.cursor()
        sql = "INSERT INTO ficha_treino (idaluno, datainicio, datavencimento) VALUES (%s, %s, %s)"
        cursor.execute(sql, (ficha.id_aluno, ficha.data_inicio, ficha.data_vencimento))
        self.conn.commit()
        cursor.close()

    def listar(self): # Nome padronizado para 'listar'
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, idaluno, datainicio, datavencimento FROM ficha_treino")
        resultados = cursor.fetchall()
        cursor.close()
        return [FichaTreino(id=r[0], id_aluno=r[1], data_inicio=r[2], data_vencimento=r[3]) for r in resultados]

    def excluir(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM ficha_treino WHERE id = %s", (id,))
        linhas = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return linhas > 0
