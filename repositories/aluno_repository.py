import psycopg2
from models.aluno import Aluno

class AlunoRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, aluno):
        cursor = self.conn.cursor()
        sql = "INSERT INTO aluno (nome, email, telefone, objetivo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (aluno.nomecompleto, aluno.email, aluno.contato, aluno.objetivo))
        self.conn.commit()
        cursor.close()

    def listar(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nome, email, telefone, objetivo FROM aluno")
        resultados = cursor.fetchall()
        cursor.close()
        return [Aluno(id=r[0], nomecompleto=r[1], email=r[2], contato=r[3], objetivo=r[4]) for r in resultados]

    def excluir(self, aluno_id):
        cursor = self.conn.cursor()
        try:
            # O rowcount nos diz quantas linhas foram deletadas
            cursor.execute("DELETE FROM aluno WHERE id = %s", (aluno_id,))
            linhas_afetadas = cursor.rowcount
            self.conn.commit()
            return linhas_afetadas > 0 # Retorna True se deletou, False se não achou
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()
