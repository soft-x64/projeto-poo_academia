from database.conexao import get_connection

def salvar_aluno(aluno):
    """Insere um novo aluno no banco de dados."""
    conexao = get_connection()
    if not conexao:
        return False
    
    sql = """
    INSERT INTO aluno (nome, cpf, email, telefone, peso, altura)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (
            aluno.nome, 
            aluno.cpf, 
            aluno.email, 
            aluno.telefone, 
            aluno.peso, 
            aluno.altura
        ))
        conexao.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"\n[ERRO BANCO]: Nao foi possivel salvar o aluno: {e}")
        return False
    finally:
        conexao.close()

def listar_alunos():
    """Busca todos os alunos cadastrados no banco."""
    conexao = get_connection()
    if not conexao:
        return []
    
    sql = "SELECT id_aluno, nome, cpf, email, telefone, peso, altura FROM aluno ORDER BY nome;"
    alunos_cadastrados = []
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        for linha in resultados:
            # Aqui mapeamos o que veio do banco para exibir no formato de dicionario ou tupla
            aluno_info = {
                "id": linha[0],
                "nome": linha[1],
                "cpf": linha[2],
                "email": linha[3],
                "telefone": linha[4],
                "peso": linha[5],
                "altura": linha[6]
            }
            alunos_cadastrados.append(aluno_info)
        cursor.close()
    except Exception as e:
        print(f"\n[ERRO BANCO]: Nao foi possivel listar os alunos: {e}")
    finally:
        conexao.close()
    return alunos_cadastrados
