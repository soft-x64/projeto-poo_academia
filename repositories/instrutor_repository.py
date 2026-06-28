import psycopg2
from models.instrutor import Instrutor

class InstrutorRepository:
    def __init__(self):
        # Certifique-se de que os dados de conexão estão corretos
        self.conn = psycopg2.connect(dbname="academia_poo", user="postgres", password="123456", host="localhost")

    def salvar(self, instrutor):
        cursor = self.conn.cursor()
        sql = "INSERT INTO instrutor (nomecompleto, cpf, email, telefone, especialidade) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (instrutor._nome, instrutor._cpf, instrutor._email, instrutor._telefone, instrutor.especialidade))
        self.conn.commit()
        cursor.close()

    def listar(self):
        cursor = self.conn.cursor()
        # Certifique-se que o nome da tabela aqui é igual ao do DELETE abaixo
        cursor.execute("SELECT id, nomecompleto, cpf, email, telefone, especialidade FROM instrutor")
        resultados = cursor.fetchall()
        cursor.close()
        return [Instrutor(id=r[0], nome=r[1], cpf=r[2], email=r[3], telefone=r[4], especialidade=r[5]) for r in resultados]

    def excluir(self, id):
        cursor = self.conn.cursor()
        try:
            # IMPORTANTE: Verifique se o nome da tabela no seu banco é realmente 'instrutor'
            cursor.execute("DELETE FROM instrutor WHERE id = %s", (id,))
            linhas_afetadas = cursor.rowcount
            self.conn.commit()
            return linhas_afetadas > 0
        except Exception as e:
            self.conn.rollback()
            print(f"Erro ao excluir: {e}")
            return False
        finally:
            cursor.close()
