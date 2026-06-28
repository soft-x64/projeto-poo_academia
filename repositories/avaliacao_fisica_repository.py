import psycopg2
from models.avaliacao_fisica import AvaliacaoFisica

class AvaliacaoFisicaRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, avaliacao):
        cursor = self.conn.cursor()
        # Usando os nomes exatos encontrados no seu banco: alunoid e data_avaliacao
        sql = "INSERT INTO avaliacao_fisica (alunoid, data_avaliacao, peso, altura) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (avaliacao.id_aluno, avaliacao.data, avaliacao.peso, avaliacao.altura))
        self.conn.commit()
        cursor.close()

    def listar_por_aluno(self, id_aluno):
        cursor = self.conn.cursor()
        # Selecionando com os nomes exatos das colunas
        query = "SELECT id, alunoid, data_avaliacao, peso, altura FROM avaliacao_fisica WHERE alunoid = %s"
        cursor.execute(query, (id_aluno,))
        resultados = cursor.fetchall()
        cursor.close()
        # Mapeando: r[0]=id, r[1]=alunoid, r[2]=data_avaliacao, r[3]=peso, r[4]=altura
        return [AvaliacaoFisica(id=r[0], id_aluno=r[1], data=r[2], peso=r[3], altura=r[4]) for r in resultados]

    def excluir(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM avaliacao_fisica WHERE id = %s", (id,))
        linhas = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return linhas > 0
