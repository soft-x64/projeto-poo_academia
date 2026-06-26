# Projeto-POO_academia

# 🏋️ TrainerX64 - Sistema de Academia (POO)

Trabalho prático desenvolvido para a disciplina de Programação Orientada a Objetos (2026.1) no ICET - UFAM.

## 👥 Integrantes
* Luiz Gustavo
* Júlio
* Eduardo
* Adriano

## 🚀 Tecnologias Utilizadas
* Python 3
* PostgreSQL (via psycopg2)  

## 📌 Funcionalidades e Conceitos de POO Aplicados
* **Classes Abstratas & Encapsulamento:** Implementados na classe base `Pessoa` e propriedades associadas.
* **Herança:** Classes `Aluno` e `Personal` herdando de `Pessoa`.
* **Polimorfismo:** Método `exibir_perfil()` chamado dinamicamente sobre uma lista misturada de usuários.
* **Regras de Negócio OO:** Bloqueio de cadastros com CPF duplicado e impedimento de criação de fichas de treino vazias (`FichaSemExercicioError`).

## 🛠️ Como Executar
1. Certifique-se de ter o PostgreSQL configurado.
2. Instale a dependência do banco de dados: `pip install psycopg2`
3. Execute o arquivo principal: `python main.py`
