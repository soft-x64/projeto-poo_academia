import psycopg2
from models.item_ficha_treino import ItemFichaTreino

class ItemFichaRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, item):
        cursor = self.conn.cursor()
        sql = "INSERT INTO item_ficha_treino (idficha, idexercicio, series, repeticoes, cargas) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (item.id_ficha, item.id_exercicio, item.series, item.repeticoes, item.cargas))
        self.conn.commit()
        cursor.close()

    def listar_da_ficha(self, id_ficha):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, idficha, idexercicio, series, repeticoes, cargas FROM item_ficha_treino WHERE idficha = %s", (id_ficha,))
        resultados = cursor.fetchall()
        cursor.close()
        return [ItemFichaTreino(id=r[0], id_ficha=r[1], id_exercicio=r[2], series=r[3], repeticoes=r[4], cargas=r[5]) for r in resultados]
