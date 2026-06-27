import psycopg2

def get_connection():
    try:
        return psycopg2.connect(
            dbname="academia_poo",  # Certifique-se que está exatamente este nome
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None
