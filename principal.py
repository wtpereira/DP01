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
tabela_categoria = []
tabela_editora = []

while True:
    print(menu_principal)
    op = input('Digite a opção: ')

    if op == '0':
        break
    elif op == '1':
        while True:
            print(menu_categoria)
            opcao_categoria = input('Digite a opção: ')
            if opcao_categoria == '2':
                nome_categoria = input('Digite o nome da categoria: ')
                nova_categoria = {
                    'nome': nome_categoria
                }
                tabela_categoria.append(nova_categoria)
                print('Categoria cadastrada com sucesso!')
                input('Digite <ENTER> para continuar...')
    elif op == '2': # else if
        while True:
            print(menu_editora)
            opcao_editora = input('Digite a opção: ')
            if opcao_editora == '2':
                nome_editora = input('Digite o nome da editora: ')
                endereco_editora = input('Digite o endereço da editora: ')
                telefone_editora = input('Digite o telefone da editora: ')
                nova_editora = {
                    'nome': nome_editora,
                    'endereco': endereco_editora,
                    'telefone': telefone_editora
                }
                tabela_editora.append(nova_editora)
                print('Categoria cadastrada com sucesso!')
                input('Digite <ENTER> para continuar...')
    elif op == '3':
        while True:
            print(menu_autor)
            opcao_autor = input('Digite a opção: ')
            if opcao_autor == '0':
                break
            elif opcao_autor == '1':
                if tabela_autores == []:
                    print('Não existem autores cadastrados.')
                else:
                    print('ID | Nome | E-mail | Telefone | Biografia')
                    for index, autor in enumerate(tabela_autores):
                        print(f"{index + 1} | {autor['nome']} | {autor['email']} | {autor['telefone']} | {autor['biografia']}")

                input('\nPressione <ENTER> para continuar...\n')
            elif opcao_autor == '2':
                nome_autor = input('Digite o nome do autor: ')
                telefone_autor = input('Digite o telefone do autor: ')
                bio_autor = input('Digite a biografia do autor: ')
                email_autor = input('Digite o e-mail do autor: ')
                novo_autor = {
                    'nome': nome_autor,
                    'email': email_autor,
                    'telefone': telefone_autor,
                    'biografia': bio_autor
                }
                tabela_autores.append(novo_autor)
                print('Autor cadastrado com sucesso!')
                input('\nPressione <ENTER> para continuar...\n')
            elif opcao_autor == '3':
                if tabela_autores == []:
                    print('Não existem autores cadastrados.')
                    input('\nPressione <ENTER> para continuar...\n')
                else:
                    id_autor = int(input('Digite o ID do autor a ser excluído: '))
                    tabela_autores.pop(id_autor - 1)
                    print('Autor excluído com sucesso!')
                    input('\nPressione <ENTER> para continuar...\n')
            elif opcao_autor == '4':
                if tabela_autores == []:
                    print('Não existem autores cadastrados.')
                    input('\nPressione <ENTER> para continuar...\n')
                else:
                    id_autor = int(input('Digite o ID do autor a ser consultado: '))
                    autor = tabela_autores[id_autor - 1]
                    print('ID | Nome | E-mail | Telefone | Biografia')
                    print(f"{id_autor} | {autor['nome']} | {autor['email']} | {autor['telefone']} | {autor['biografia']}")
                    input('\nPressione <ENTER> para continuar...\n')
            elif opcao_autor == '5':
                if tabela_autores == []:
                    print('Não existem autores cadastrados.')
                    input('\nPressione <ENTER> para continuar...\n')
                else:
                    id_autor = int(input('Digite o ID do autor a ser editado: '))
                    autor = tabela_autores[id_autor - 1]

                    nome_autor = input('Digite o nome do autor: ')
                    telefone_autor = input('Digite o telefone do autor: ')
                    bio_autor = input('Digite a biografia do autor: ')
                    email_autor = input('Digite o e-mail do autor: ')

                    autor['nome'] = nome_autor
                    autor['email'] = email_autor
                    autor['telefone'] = telefone_autor
                    autor['biografia'] = bio_autor

                    print('Autor editado com sucesso!')
                    input('\nPressione <ENTER> para continuar...\n')
            else:
                print('Opção inválida!')
    elif op == '4':
        print(menu_livro)
        input('Digite <ENTER> para continuar...')
    else:
        print('Opção inválida!')

print('Programa encerrado!')

