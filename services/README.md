# Pasta services

Esta pasta é responsável pelas regras de negócio do sistema.

## O que deve ser colocado aqui

- Validações antes de salvar dados.
- Regras de funcionamento do sistema.
- Processamento de informações antes de enviar para o banco.
- Comunicação entre a interface e os repositórios.

## Exemplos de arquivos futuros

- `aluno_service.py`  
  Responsável pelas regras relacionadas ao cadastro e gerenciamento de alunos.

- `treino_service.py`  
  Responsável pelas regras relacionadas aos treinos.

- `mensalidade_service.py`  
  Responsável pelas regras relacionadas aos pagamentos e cobranças.

## Exemplos de responsabilidades

- Verificar se os campos obrigatórios foram preenchidos.
- Validar se o e-mail do aluno é válido.
- Verificar se uma mensalidade já foi paga.
- Impedir cadastro duplicado.
- Organizar os dados antes de enviar para o repository.

## Responsabilidade da equipe

Quem trabalhar nesta pasta deve concentrar a lógica principal do sistema.  
A pasta services não deve acessar diretamente a interface visual e deve usar os repositories para lidar com o banco de dados.