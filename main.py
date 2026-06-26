import sys
from ui.menu_principal import exibir_menu_principal

def main():
    # Listas em memória que simulam as tabelas do banco de dados temporariamente
    lista_alunos = []
    lista_personais = []
    lista_aparelhos = []
    lista_exercicios = []
    lista_avaliacoes = []
    lista_fichas = []

    try:
        exibir_menu_principal(
            lista_alunos, 
            lista_personais, 
            lista_aparelhos, 
            lista_exercicios, 
            lista_avaliacoes, 
            lista_fichas
        )
    except KeyboardInterrupt:
        print("\nSistema encerrado de forma forcada. Ate logo!")
        sys.exit(0)

if __name__ == "__main__":
    main()
