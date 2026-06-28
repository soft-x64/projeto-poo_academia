import psycopg2
from models.aparelho import Aparelho

class AparelhoRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, aparelho):
        cursor = self.conn.cursor()
        # Certifique-se de que o nome da coluna no SQL é 'grupomuscular'
        sql = "INSERT INTO aparelho (nome, grupomuscular) VALUES (%s, %s)"
        cursor.execute(sql, (aparelho.nome, aparelho.grupoMuscular))
        self.conn.commit()
        cursor.close()

    def listar(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, grupomuscular FROM aparelho")
        resultados = cursor.fetchall()
        cursor.close()
        # Converte tupla (id, nome, grupomuscular) para Objeto Aparelho
        return [Aparelho(id=r[0], nome=r[1], grupoMuscular=r[2]) for r in resultados]

    def excluir(self, id_aparelho):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM aparelho WHERE id = %s", (id_aparelho,))
        self.conn.commit()
        cursor.close()
