import psycopg2
from models.avaliacao_fisica import AvaliacaoFisica

class AvaliacaoFisicaRepository:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=academia_poo user=postgres password=123456 host=localhost")

    def salvar(self, av):
        cursor = self.conn.cursor()
        sql = """INSERT INTO avaliacao_fisica (alunoid, instrutorid, peso, altura, imc) 
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (av.alunoId, av.instrutorId, av.peso, av.altura, av.imc))
        self.conn.commit()
        cursor.close()

    def buscar_por_aluno(self, aluno_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, alunoid, instrutorid, data_avaliacao, peso, altura, imc FROM avaliacao_fisica WHERE alunoid = %s", (aluno_id,))
        resultados = cursor.fetchall()
        cursor.close()
        return [AvaliacaoFisica(r[0], r[1], r[2], r[3], r[4], r[5], r[6]) for r in resultados]
