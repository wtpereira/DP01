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

tabela_autores = []

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
        while True:
            print(menu_autor)
            opcao_autor = input('Digite a opção: ')
            if opcao_autor == '0':
                break
            elif opcao_autor == '1':
                print('Nome | E-mail | Telefone | Biografia')
                for autor in tabela_autores:
                    print(f'{autor[0]} | {autor[1]} | {autor[2]} | {autor[3]}')
            elif opcao_autor == '2':
                nome_autor = input('Digite o nome do autor: ')
                telefone_autor = input('Digite o telefone do autor: ')
                bio_autor = input('Digite a biografia do autor: ')
                email_autor = input('Digite o e-mail do autor: ')
                novo_autor = []
                novo_autor.append(nome_autor)
                novo_autor.append(email_autor)
                novo_autor.append(telefone_autor)
                novo_autor.append(bio_autor)
                tabela_autores.append(novo_autor)
            elif opcao_autor == '3':
                print('3')
            elif opcao_autor == '4':
                print('4')
            elif opcao_autor == '5':
                print('5')
            else:
                print('Opção inválida!')
    elif op == '4':
        print(menu_livro)
        input('Digite <ENTER> para continuar...')
    else:
        print('Opção inválida!')

print('Programa encerrado!')

