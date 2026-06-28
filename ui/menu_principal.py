from ui.menu_aluno import sub_menu_aluno
from ui.menu_instrutor import sub_menu_instrutor
from ui.menu_aparelho import sub_menu_aparelho
from ui.menu_exercicio import sub_menu_exercicio
from ui.menu_ficha import sub_menu_ficha
from ui.menu_avaliacao_fisica import sub_menu_avaliacao_fisica

def exibir_menu_principal(aluno_s, instrutor_s, aparelho_s, exercicio_s, ficha_s, ficha_ex_s, avaliacao_s):
    while True:
        print("\n--- SISTEMA DE ACADEMIA ---")
        print("1. Alunos | 2. Instrutores | 3. Aparelhos | 4. Exercícios | 5. Fichas | 6. Avaliações | 7. Sair")
        opcao = input("Escolha: ")
        
        if opcao == "1": sub_menu_aluno(aluno_s)
        elif opcao == "2": sub_menu_instrutor(instrutor_s)
        elif opcao == "3": sub_menu_aparelho(aparelho_s)
        elif opcao == "4": sub_menu_exercicio(exercicio_s)
        elif opcao == "5": sub_menu_ficha(ficha_s) 
        elif opcao == "6": sub_menu_avaliacao_fisica(avaliacao_s)
        elif opcao == "7": break
