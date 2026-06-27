-- Script de Criação do Banco de Dados Academia
-- Execute este script no seu PostgreSQL para configurar o ambiente

CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE instrutor (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    especialidade VARCHAR(100)
);

CREATE TABLE aparelho (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE exercicio (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    aparelho_id INTEGER REFERENCES aparelho(id)
);

CREATE TABLE ficha_treino (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER REFERENCES aluno(id),
    instrutor_id INTEGER REFERENCES instrutor(id),
    descricao VARCHAR(255)
);

CREATE TABLE avaliacao_fisica (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER REFERENCES aluno(id),
    data_avaliacao DATE,
    peso DECIMAL(5,2),
    altura DECIMAL(3,2)
);
