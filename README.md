# 🏋️ TrainerX64 — Sistema de Gerenciamento de Academia

Trabalho Prático desenvolvido para a disciplina de Programação Orientada a Objetos (POO), sob orientação do Prof. Alternei Brito. O sistema estende os modelos físicos de banco de dados desenvolvidos previamente e os integra a uma arquitetura limpa em camadas utilizando Python 3 e persistência relacional com PostgreSQL.

##  Integrantes do Grupo
* **Adriano** — Desenvolvimento da Camada de Serviços (`services/`), Menu Interativo (`ui/`), Tratamento de Exceções de Segurança e Documentação.
* **Eduardo** — Implementação do Script de Conexão com PostgreSQL, Criação de tabelas com `psycopg2` e Camada de Repositórios (`repositories/`).
* **Júlio & Luiz Gustavo** — Modelagem Orientada a Objetos das Classes de Domínio (`models/`), Abstrações, Herança e Encapsulamento.

##  Tecnologias Utilizadas
* **Python 3.x**
* **PostgreSQL**
* **Módulo psycopg2-binary** (Acesso nativo sem uso de frameworks/ORMs)

##  Estrutura do Projeto (Arquitetura em Camadas)
* `models/`: Entidades de domínio (Pessoa, Aluno, Instrutor, etc.) contendo encapsulamento e regras básicas.
* `repositories/`: Código focado em comandos SQL nativos e comunicação direta com o banco.
* `services/`: Validação de regras corporativas (ex: bloqueio de CPFs duplicados).
* `ui/`: Menus textuais e segurança de dados do terminal.
* `database/`: Controle de conexões do driver de banco.

##  Conceitos de POO Aplicados no Projeto
1. **Abstração (ABC):** A classe `Pessoa` é definida como uma classe abstrata que obriga a implementação do método `exibir_perfil()`.
2. **Herança:** `Aluno` e `Instrutor` herdam os atributos e comportamentos comuns definidos na classe abstrata `Pessoa`.
3. **Encapsulamento:** Atributos restritos protegidos e gerenciados por setters e getters internos.
4. **Polimorfismo:** Execução de rotinas customizadas por tipo de objeto a partir de uma lista genérica de `Pessoa` ao invocar `exibir_perfil()`.

#  Sistema de Gestão de Academia (POO)

Projeto desenvolvido como parte da disciplina de Programação Orientada a Objetos, com o objetivo de gerenciar o fluxo operacional de uma academia, incluindo alunos, instrutores, fichas de treino e avaliações físicas.

---

## Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Banco de Dados:** PostgreSQL
* **Driver de Conexão:** psycopg2-binary
* **Paradigma:** Programação Orientada a Objetos (POO)

---

##  Como Executar o Projeto

Siga os passos abaixo para configurar o ambiente em sua máquina local:

### 1. Pré-requisitos
Certifique-se de ter instalado:
* [Python 3.x](https://www.python.org/downloads/)
* [PostgreSQL](https://www.postgresql.org/download/)

### 2. Preparação do Ambiente
Clone o repositório e acesse a pasta:

```bash
git clone https://github.com/soft-x64/projeto-poo_academia.git
cd projeto-poo_academia
```

Instale a dependência necessária para a conexão com o banco de dados:

```bash
pip install psycopg2-binary
```
3. Configuração do Banco de Dados
No seu gerenciador PostgreSQL (psql ou pgAdmin), crie o banco de dados:
SQL
```bash
CREATE DATABASE academia_poo;
```
Atenção: Verifique nos arquivos dentro da pasta repositories/ se o usuário e a senha do banco (user: postregs e password:123456) coincidem com a sua instalação local. Se forem diferentes, atualize os arquivos antes de rodar o sistema.

4. Execução
Com o banco criado e as dependências instaladas, execute o sistema pelo terminal:
```bash
python main.py
```
