import psycopg2
from models.avaliacao_fisica import AvaliacaoFisica

class AvaliacaoFisicaRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, av):
        cursor = self.conn.cursor()
        sql = "INSERT INTO avaliacao_fisica (alunoid, instrutorid, peso, altura, imc) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (av.id_aluno, av.id_instrutor, av.peso, av.altura, av.imc))
        self.conn.commit()
        cursor.close()

    def buscar_por_aluno(self, id_aluno):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, alunoid, instrutorid, data_avaliacao, peso, altura, imc FROM avaliacao_fisica WHERE alunoid = %s", (id_aluno,))
        resultados = cursor.fetchall()
        cursor.close()
        return [AvaliacaoFisica(id=r[0], id_aluno=r[1], id_instrutor=r[2], data=r[3], peso=r[4], altura=r[5], imc=r[6]) for r in resultados]
