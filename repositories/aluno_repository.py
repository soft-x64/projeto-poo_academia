import psycopg2
from models.aluno import Aluno

class AlunoRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, aluno):
        cursor = self.conn.cursor()
        # Nota: usamos aluno._nome, aluno._email, etc.
        sql = "INSERT INTO aluno (nome, email, telefone, objetivo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (aluno._nome, aluno._email, aluno._telefone, aluno.objetivo))
        self.conn.commit()
        cursor.close()

    def listar(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, email, telefone, objetivo FROM aluno")
        resultados = cursor.fetchall()
        cursor.close()
        # O construtor Aluno agora recebe os atributos padronizados
        return [Aluno(id=r[0], nome=r[1], email=r[2], telefone=r[3], objetivo=r[4]) for r in resultados]

    def excluir(self, aluno_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM aluno WHERE id = %s", (aluno_id,))
        self.conn.commit()
        cursor.close()
        return cursor.rowcount > 0
