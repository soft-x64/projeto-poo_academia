import psycopg2
from psycopg2 import OperationalError

def get_connection():
    try:
        conexao = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123456",
            port="5433"
        )
        return conexao
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL na porta 5433: {e}")
        return None
