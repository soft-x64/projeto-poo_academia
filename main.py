import sys
from ui.menu_principal import exibir_menu_principal
from database.services import AlunoService, InstrutorRepository

def main():
    # Cria os objetos que o Júlio espera receber nos menus
    aluno_service = AlunoService()
    instrutor_repository = InstrutorRepository()

    try:
        # Passa os serviços para o menu principal que agora está dentro da pasta ui
        exibir_menu_principal(aluno_service, instrutor_repository)
    except KeyboardInterrupt:
        print("\nSistema encerrado. Ate logo!")
        sys.exit(0)

if __name__ == "__main__":
    main()
