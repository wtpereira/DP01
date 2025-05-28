from model.autor import Autor

from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService
from service.livro_service import LivroService

menu_principal = """
\033[0;32m[Menu Principal] Escolha uma das seguintes opções:\033[0m
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""

def main():
    autor_service = AutorService()
    categoria_service = CategoriaService()
    editora_service = EditoraService()
    livro_service = LivroService()

    while True:
        print(menu_principal)
        op = input('Digite a opção: ')

        match op:
            case '0':
                break
            case '1':
                categoria_service.menu()
            case '2':
                editora_service.menu()
            case '3':
                autor_service.menu()
            case '4':
                livro_service.menu()
            case _:
                print('Opção inválida!')
                input()

    print('Programa encerrado!')

if __name__ == '__main__':
    main()
