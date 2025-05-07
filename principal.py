menu_principal = """
[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa
"""

menu_categoria = """
[Categorias] Escolha uma das seguintes opções:
1 - Listar toda as categorias
2 - Adicionar nova categoria
3 - Excluir categoria
4 - Ver categoria por Id
0 - Voltar ao menu anterior
"""

menu_editora = """
[Editoras] Escolha uma das seguintes opções:
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior
"""

menu_autor = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
5 - Editar autor
0 - Voltar ao menu anterior
"""

menu_livro = """
[Livros] Escolha uma das seguintes opções:
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
0 - Voltar ao menu anterior
"""

while True:
    print(menu_principal)
    op = input('Digite a opção: ')

    if op == '0':
        break
    elif op == '1':
        print(menu_categoria)
        input('Digite <ENTER> para continuar...')
    elif op == '2': # else if
        print(menu_editora)
        input('Digite <ENTER> para continuar...')
    elif op == '3':
        print(menu_autor)
        input('Digite <ENTER> para continuar...')
    elif op == '4':
        print(menu_livro)
        input('Digite <ENTER> para continuar...')
    else:
        print('Opção inválida!')

print('Programa encerrado!')

