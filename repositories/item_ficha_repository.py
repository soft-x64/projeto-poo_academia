import psycopg2
from models.item_ficha_treino import ItemFichaTreino

class ItemFichaRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, item):
        cursor = self.conn.cursor()
        sql = "INSERT INTO item_ficha_treino (idficha, idexercicio, series, repeticoes, cargas) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (item.idFicha, item.idExercicio, item.series, item.repeticoes, item.cargas))
        self.conn.commit()
        cursor.close()

    def listar_da_ficha(self, id_ficha):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, idficha, idexercicio, series, repeticoes, cargas FROM item_ficha_treino WHERE idficha = %s", (id_ficha,))
        resultados = cursor.fetchall()
        cursor.close()
        return [ItemFichaTreino(r[0], r[1], r[2], r[3], r[4], r[5]) for r in resultados]
