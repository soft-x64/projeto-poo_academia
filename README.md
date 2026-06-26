# 🏋️ TrainerX64 — Sistema de Gerenciamento de Academia

Trabalho Prático desenvolvido para a disciplina de Programação Orientada a Objetos (POO), sob orientação do Prof. Alternei Brito. O sistema estende os modelos físicos de banco de dados desenvolvidos previamente e os integra a uma arquitetura limpa em camadas utilizando Python 3 e persistência relacional com PostgreSQL.

## 👥 Integrantes do Grupo
* **Adriano** — Desenvolvimento da Camada de Serviços (`services/`), Menu Interativo (`ui/`), Tratamento de Exceções de Segurança e Documentação.
* **Eduardo** — Implementação do Script de Conexão com PostgreSQL, Criação de tabelas com `psycopg2` e Camada de Repositórios (`repositories/`).
* **Júlio & Luiz Gustavo** — Modelagem Orientada a Objetos das Classes de Domínio (`models/`), Abstrações, Herança e Encapsulamento.

## 🚀 Tecnologias Utilizadas
* **Python 3.x**
* **PostgreSQL**
* **Módulo psycopg2-binary** (Acesso nativo sem uso de frameworks/ORMs)

## 🏗️ Estrutura do Projeto (Arquitetura em Camadas)
* `models/`: Entidades de domínio (Pessoa, Aluno, Instrutor, etc.) contendo encapsulamento e regras básicas.
* `repositories/`: Código focado em comandos SQL nativos e comunicação direta com o banco.
* `services/`: Validação de regras corporativas (ex: bloqueio de CPFs duplicados).
* `ui/`: Menus textuais e segurança de dados do terminal.
* `database/`: Controle de conexões do driver de banco.

## 🧠 Conceitos de POO Aplicados no Projeto
1. **Abstração (ABC):** A classe `Pessoa` é definida como uma classe abstrata que obriga a implementação do método `exibir_perfil()`.
2. **Herança:** `Aluno` e `Instrutor` herdam os atributos e comportamentos comuns definidos na classe abstrata `Pessoa`.
3. **Encapsulamento:** Atributos restritos protegidos e gerenciados por setters e getters internos.
4. **Polimorfismo:** Execução de rotinas customizadas por tipo de objeto a partir de uma lista genérica de `Pessoa` ao invocar `exibir_perfil()`.

## 🛠️ Como Executar o Projeto
1. Certifique-se de possuir o PostgreSQL instalado e rodando em sua máquina.
2. Configure as credenciais de acesso dentro de `database/connection.py`.
3. Instale a biblioteca do driver utilizando o terminal:
   ```bash
   pip install psycopg2-binary
