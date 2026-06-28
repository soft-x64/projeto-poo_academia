DROP TABLE IF EXISTS item_ficha_treino;
DROP TABLE IF EXISTS ficha_treino;
DROP TABLE IF EXISTS avaliacao_fisica;
DROP TABLE IF EXISTS exercicio;
DROP TABLE IF EXISTS aparelho;
DROP TABLE IF EXISTS instrutor;
DROP TABLE IF EXISTS aluno;

CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20),
    objetivo VARCHAR(100)
);

CREATE TABLE instrutor (
    id SERIAL PRIMARY KEY,
    nomecompleto VARCHAR(100),
    cpf VARCHAR(20),
    email VARCHAR(100),
    telefone VARCHAR(20),
    especialidade VARCHAR(100)
);

CREATE TABLE aparelho (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    grupomuscular VARCHAR(100)
);

CREATE TABLE exercicio (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    grupomuscular VARCHAR(100),
    descricaoaudio TEXT,
    idaparelho INTEGER REFERENCES aparelho(id)
);

CREATE TABLE ficha_treino (
    id SERIAL PRIMARY KEY,
    idaluno INTEGER REFERENCES aluno(id),
    datainicio DATE,
    datavencimento DATE
);

CREATE TABLE item_ficha_treino (
    id SERIAL PRIMARY KEY,
    idficha INTEGER REFERENCES ficha_treino(id) ON DELETE CASCADE,
    idexercicio INTEGER REFERENCES exercicio(id),
    series INTEGER,
    repeticoes INTEGER,
    cargas DECIMAL(5,2)
);

CREATE TABLE avaliacao_fisica (
    id SERIAL PRIMARY KEY,
    alunoid INTEGER REFERENCES aluno(id),
    instrutorid INTEGER REFERENCES instrutor(id),
    data_avaliacao DATE DEFAULT CURRENT_DATE,
    peso DECIMAL(5,2),
    altura DECIMAL(3,2),
    imc DECIMAL(5,2)
);
