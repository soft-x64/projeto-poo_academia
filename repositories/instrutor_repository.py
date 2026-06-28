import psycopg2
from models.instrutor import Instrutor

class InstrutorRepository:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, instrutor):
        cursor = self.conn.cursor()
        sql = "INSERT INTO instrutor (nomecompleto, cpf, email, telefone, especialidade) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (instrutor.nomecompleto, instrutor.cpf, instrutor.email, instrutor.telefone, instrutor.especialidade))
        self.conn.commit()
        cursor.close()

    def listar(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, nomecompleto, cpf, email, telefone, especialidade FROM instrutor")
        resultados = cursor.fetchall()
        cursor.close()
        return [Instrutor(id=r[0], nomecompleto=r[1], cpf=r[2], email=r[3], telefone=r[4], especialidade=r[5]) for r in resultados]

    def excluir(self, instrutor_id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("DELETE FROM instrutor WHERE id = %s", (instrutor_id,))
            linhas_afetadas = cursor.rowcount
            self.conn.commit()
            return linhas_afetadas > 0  # Retorna True se deletou, False se o ID não existia
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()
