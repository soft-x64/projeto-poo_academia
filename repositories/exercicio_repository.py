import psycopg2
from models.exercicio import Exercicio

class ExercicioRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, exercicio):
        cursor = self.conn.cursor()
        # O banco espera 'grupomuscular' e 'idaparelho'
        sql = "INSERT INTO exercicio (nome, grupomuscular, idaparelho) VALUES (%s, %s, %s)"
        cursor.execute(sql, (exercicio.nome, exercicio.grupo_muscular, exercicio.id_aparelho))
        self.conn.commit()
        cursor.close()

    def listar(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, grupomuscular, idaparelho FROM exercicio")
        resultados = cursor.fetchall()
        cursor.close()
        # Converte as colunas do banco para os atributos do objeto
        return [Exercicio(id=r[0], nome=r[1], grupo_muscular=r[2], id_aparelho=r[3]) for r in resultados]

    def excluir(self, id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM exercicio WHERE id = %s", (id,))
        linhas = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return linhas > 0
