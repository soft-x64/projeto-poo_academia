from database.conexao import get_connection

def criar_tabelas():
    """Cria as tabelas do sistema no banco de dados se elas nao existirem."""
    
    sql_tabelas = """
    CREATE TABLE IF NOT EXISTS instrutor (
        id_instrutor SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        cpf VARCHAR(11) UNIQUE NOT NULL,
        email VARCHAR(100),
        telefone VARCHAR(20),
        cref VARCHAR(50) UNIQUE NOT NULL,
        especialidade VARCHAR(100)
    );

    CREATE TABLE IF NOT EXISTS aluno (
        id_aluno SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        cpf VARCHAR(11) UNIQUE NOT NULL,
        email VARCHAR(100),
        telefone VARCHAR(20),
        peso NUMERIC(5,2) NOT NULL,
        altura NUMERIC(3,2) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS aparelho (
        id_aparelho SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        tipo VARCHAR(50),
        capacidade_carga NUMERIC(5,2)
    );

    CREATE TABLE IF NOT EXISTS exercicio (
        id_exercicio SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        grupo_muscular VARCHAR(50) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS ficha_treino (
        id_ficha SERIAL PRIMARY KEY,
        id_aluno INT REFERENCES aluno(id_aluno) ON DELETE CASCADE,
        id_instrutor INT REFERENCES instrutor(id_instrutor) ON DELETE SET NULL,
        data_criacao DATE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS item_ficha (
        id_item SERIAL PRIMARY KEY,
        id_ficha INT REFERENCES ficha_treino(id_ficha) ON DELETE CASCADE,
        id_exercicio INT REFERENCES exercicio(id_exercicio) ON DELETE CASCADE,
        series INT NOT NULL,
        repeticoes INT NOT NULL,
        carga NUMERIC(5,2) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS avaliacao_fisica (
        id_avaliacao SERIAL PRIMARY KEY,
        id_aluno INT REFERENCES aluno(id_aluno) ON DELETE CASCADE,
        id_instrutor INT REFERENCES instrutor(id_instrutor) ON DELETE SET NULL,
        data_avaliacao DATE NOT NULL,
        percentual_gordura NUMERIC(4,1) NOT NULL,
        observacoes TEXT
    );
    """

    conexao = get_connection()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql_tabelas)
            conexao.commit()
            print("[SUCESSO] Tabelas criadas ou ja existentes no banco de dados!")
            cursor.close()
        except Exception as e:
            print(f"[ERRO SQL]: Falha ao estruturar as tabelas: {e}")
        finally:
            conexao.close()

if __name__ == "__main__":
    criar_tabelas()
