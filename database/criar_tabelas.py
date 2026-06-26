from database.connection import get_connection

def create_tables():
    """
    Executa os comandos DDL para criar as tabelas do sistema de academia.
    As tabelas herdam o mapeamento do projeto de Banco de Dados I.
    """
    commands = [
        # 1. Tabela Base: Aluno
        """
        CREATE TABLE IF NOT EXISTS aluno (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cpf VARCHAR(14) UNIQUE NOT NULL,
            email VARCHAR(100),
            telefone VARCHAR(20)
        );
        """,
        # 2. Tabela: Instrutor
        """
        CREATE TABLE IF NOT EXISTS instrutor (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            cpf VARCHAR(14) UNIQUE NOT NULL,
            email VARCHAR(100),
            telefone VARCHAR(20),
            cref VARCHAR(20) UNIQUE NOT NULL
        );
        """,
        # 3. Tabela: Aparelho
        """
        CREATE TABLE IF NOT EXISTS aparelho (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            descricao VARCHAR(200)
        );
        """,
        # 4. Tabela: Exercicio
        """
        CREATE TABLE IF NOT EXISTS exercicio (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            grupo_muscular VARCHAR(50),
            id_aparelho INT REFERENCES aparelho(id) ON DELETE SET NULL
        );
        """,
        # 5. Tabela: Ficha de Treino
        """
        CREATE TABLE IF NOT EXISTS ficha_treino (
            id SERIAL PRIMARY KEY,
            id_aluno INT NOT NULL REFERENCES aluno(id) ON DELETE CASCADE,
            id_instrutor INT REFERENCES instrutor(id) ON DELETE SET NULL,
            data_criacao DATE DEFAULT CURRENT_DATE,
            objetivo VARCHAR(100)
        );
        """,
        # 6. Tabela Pivot / Relacionamento N:M (Ficha -> Exercício)
        """
        CREATE TABLE IF NOT EXISTS ficha_exercicio (
            id_ficha INT REFERENCES ficha_treino(id) ON DELETE CASCADE,
            id_exercicio INT REFERENCES exercicio(id) ON DELETE CASCADE,
            series INT NOT NULL,
            repeticoes INT NOT NULL,
            carga VARCHAR(20),
            PRIMARY KEY (id_ficha, id_exercicio)
        );
        """,
        # 7. Tabela: Avaliação Física
        """
        CREATE TABLE IF NOT EXISTS avaliacao_fisica (
            id SERIAL PRIMARY KEY,
            id_aluno INT NOT NULL REFERENCES aluno(id) ON DELETE CASCADE,
            id_instrutor INT REFERENCES instrutor(id) ON DELETE SET NULL,
            data_avaliacao DATE DEFAULT CURRENT_DATE,
            peso NUMERIC(5,2),
            altura NUMERIC(3,2),
            gordura_corporal NUMERIC(4,1)
        );
        """
    ]

    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Executa cada um dos comandos de criação
        for command in commands:
            cursor.execute(command)
            
        conn.commit()
        cursor.close()
        print("[DATABASE]: Todas as tabelas foram validadas/criadas com sucesso!")
        
    except Exception as e:
        print(f"[ERRO SQL]: Falha ao estruturar as tabelas do sistema. {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Permite rodar diretamente o arquivo para testar a criação das tabelas
    create_tables()
