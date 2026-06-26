import sys
from ui.menu_usuarios import menu_usuarios
from ui.menu_equipamentos import menu_equipamentos
from ui.menu_avaliacoes import menu_avaliacoes
from ui.menu_fichas import menu_fichas

def exibir_menu_principal(lista_alunos, lista_personais, lista_aparelhos, lista_exercicios, lista_avaliacoes, lista_fichas):
    while True:
        print("\n" + "="*40)
        print("SISTEMA DE ACADEMIA - PRINCIPAL")
        print("="*40)
        print("1. Menu Usuarios (Alunos / Personais)")
        print("2. Menu Equipamentos e Exercicios")
        print("3. Menu Avaliacoes Fisicas")
        print("4. Menu Fichas de Treino")
        print("5. Sair do Sistema")
        print("="*40)
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao == '1':
            menu_usuarios(lista_alunos, lista_personais)
        elif opcao == '2':
            menu_equipamentos(lista_aparelhos, lista_exercicios)
        elif opcao == '3':
            menu_avaliacoes(lista_alunos, lista_avaliacoes)
        elif opcao == '4':
            menu_fichas(lista_alunos, lista_personais, lista_exercicios, lista_fichas)
        elif opcao == '5':
            print("\nEncerrando o sistema. Ate logo!")
            sys.exit(0)
        else:
            print("\nErro: Opcao invalida. Tente novamente.")
