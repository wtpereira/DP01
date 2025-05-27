from model.autor import Autor

from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService

menu_principal = """
\033[0;32m[Menu Principal] Escolha uma das seguintes opções:\033[0m
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""

menu_livro = """
\033[0;34m[Livros] Escolha uma das seguintes opções:\033[0m
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
5 - Editar livro
0 - Voltar ao menu anterior
"""

autor_service = AutorService()
categoria_service = CategoriaService()
editora_service = EditoraService()

tabela_autores = []
tabela_categorias = []
tabela_editoras = []
tabela_livros = []


def organiza_livro():
    print(menu_livro)
    opcao_livro = input('Digite a opção: ')
    if opcao_livro == '0':
        return
    elif opcao_livro == '1':
        if tabela_livros == []:
            print('Não existem livros cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            print('ID | Título | Ano | Qtde páginas | ISBN | Resumo | Autor | Categoria | Editora')
            for index, livro in enumerate(tabela_livros):
                print(f"{index + 1} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['resumo']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_livro == '2':
        if tabela_autores == [] or tabela_categorias == [] or tabela_editoras == []:
            print('É necessário pelo menos um autor, uma categoria, e uma editora cadastros.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            titulo = input('Digite o título do livro: ')
            resumo = input('Digite o resumo do livro: ')
            ano = input('Digite o ano de publicação do livro: ')
            paginas = input('Digite a quantidade de páginas: ')
            isbn = input('Digite o ISBN do livro: ')
            id_autor = int(input('Digite o ID do autor: '))
            id_categoria = int(input('Digite o ID da categoria: '))
            id_editora = int(input('Digite o ID da editora: '))

            novo_livro = {
                'titulo': titulo,
                'resumo': resumo,
                'ano': ano,
                'paginas': paginas,
                'isbn': isbn,
                'autor': tabela_autores[id_autor -1],
                'categoria': tabela_categorias[id_categoria -1],
                'editora': tabela_editoras[id_editora - 1]
            }
            tabela_livros.append(novo_livro)
            print('Livro cadastrado com sucesso!')
            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_livro == '3':
        if tabela_livros == []:
            print('Não existem livros cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_livro = int(input('Digite o ID do livro a ser excluído: '))
                tabela_livros.pop(id_livro - 1)
                print('Livro excluído com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_livro == '4':
        if tabela_livros == []:
            print('Não existem livros cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_livro = int(input('Digite o ID do livro a ser consultado: '))
                livro = tabela_livros[id_livro - 1]
                print('ID | Título | Ano | Qtde páginas | ISBN | Resumo | Autor | Categoria | Editora')
                print(f"{id_livro} | {livro['titulo']} | {livro['ano']} | {livro['paginas']} | {livro['isbn']} | {livro['resumo']} | {livro['autor']['nome']} | {livro['categoria']['nome']} | {livro['editora']['nome']}")
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_livro == '5':
        if tabela_livros == []:
            print('Não existem livros cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            if tabela_autores == [] or tabela_categorias == [] or tabela_editoras == []:
                print('É necessário pelo menos um autor, uma categoria, e uma editora cadastros.')
                input('\nPressione <ENTER> para continuar...\n')
            else:
                id_livro = int(input('Digite o ID do livro a ser editado: '))
                livro = tabela_livros[id_livro - 1]
                titulo = input('Digite o título do livro: ')
                resumo = input('Digite o resumo do livro: ')
                ano = input('Digite o ano de publicação do livro: ')
                paginas = input('Digite a quantidade de páginas: ')
                isbn = input('Digite o ISBN do livro: ')
                id_autor = int(input('Digite o ID do autor: '))
                id_categoria = int(input('Digite o ID da categoria: '))
                id_editora = int(input('Digite o ID da editora: '))
                livro['titulo'] = titulo
                livro['resumo'] = resumo
                livro['ano'] = ano
                livro['paginas'] = paginas
                livro['isbn'] = isbn
                livro['autor'] = tabela_autores[id_autor -1]
                livro['categoria'] = tabela_categorias[id_categoria -1]
                livro['editora'] = tabela_editoras[id_editora - 1]

                print('Livro editado com sucesso!')
                input('\nPressione <ENTER> para continuar...\n')
    else:
        print('Opção inválida!')
        input()

    organiza_livro()


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
            organiza_livro()
        case _:
            print('Opção inválida!')
            input()

print('Programa encerrado!')

