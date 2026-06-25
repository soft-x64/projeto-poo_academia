# Pasta repositories

Esta pasta é responsável pela comunicação direta entre o sistema e o banco de dados.

## O que deve ser colocado aqui

- Arquivos que realizam operações no banco de dados.
- Funções de cadastro, busca, atualização e remoção de dados.
- Consultas SQL organizadas por entidade do sistema.

## Exemplos de arquivos futuros

- `aluno_repository.py`  
  Responsável pelas operações de banco relacionadas aos alunos.

- `treino_repository.py`  
  Responsável pelas operações de banco relacionadas aos treinos.

- `mensalidade_repository.py`  
  Responsável pelas operações de banco relacionadas às mensalidades.

## Exemplos de responsabilidades

- Cadastrar aluno no banco.
- Buscar aluno pelo ID.
- Listar alunos cadastrados.
- Atualizar dados de mensalidade.
- Remover registros quando necessário.

## Responsabilidade da equipe

Quem trabalhar nesta pasta deve evitar colocar regras de negócio aqui.  
Esta camada deve focar apenas no acesso e manipulação dos dados no banco.