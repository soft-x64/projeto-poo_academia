import psycopg2
from models.exercicio import Exercicio

class ExercicioRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, exercicio):
        cursor = self.conn.cursor()
        sql = "INSERT INTO exercicio (nome, grupomuscular, descricaoaudio, idaparelho) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (exercicio.nome, exercicio.grupomuscular, exercicio.descricaoaudio, exercicio.idaparelho))
        self.conn.commit()
        cursor.close()

    def listar(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, grupomuscular, descricaoaudio, idaparelho FROM exercicio")
        resultados = cursor.fetchall()
        cursor.close()
        return [Exercicio(id=r[0], nome=r[1], grupomuscular=r[2], descricaoaudio=r[3], idaparelho=r[4]) for r in resultados]

    def excluir(self, id_exercicio):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM exercicio WHERE id = %s", (id_exercicio,))
        self.conn.commit()
        cursor.close()
