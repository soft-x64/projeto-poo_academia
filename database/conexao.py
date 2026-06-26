import psycopg2
from psycopg2 import OperationalError

# Configurações o banco de dados local do Postgres
# Da pra alterar os valores abaixo de acordo com as credenciais que nós for usar
DB_SETTINGS = {
    "dbname": "trainerx64",
    "user": "postgres",
    "password": "sua_senha_aqui",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    """
    Retorna uma conexão ativa com o banco de dados PostgreSQL.
    Lança uma exceção controlada caso falhe.
    """
    try:
        connection = psycopg2.connect(**DB_SETTINGS)
        return connection
    except OperationalError as e:
        print(f"[ERRO DE CONEXÃO]: Não foi possível conectar ao PostgreSQL. {e}")
        raise e
