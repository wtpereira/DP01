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
5 - Editar categoria
0 - Voltar ao menu anterior
"""

menu_editora = """
[Editoras] Escolha uma das seguintes opções:
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
5 - Editar editora
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
5 - Editar livro
0 - Voltar ao menu anterior
"""

tabela_autores = []
tabela_categorias = []
tabela_editoras = []
tabela_livros = []


def email_valido(email):
    if email.find('@') >= 1 and email.find('.com') >= 3:
        return True
    else:
        return False

class Autor:
    __slots__ = ['__nome', '__email', '__telefone', '__biografia']

    def __init__(self, n, e, t, b):  # construtor ou inicializador
        self.nome = n
        self.email = e
        self.telefone = t
        self.biografia = b

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        self.__nome = n.title()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, e):
        e = e.lower()  # Transformar para minúsculo.
        if email_valido(e):
            self.__email = e
            return
        else:
            self.__email = None
            raise Exception('E-mail inválido!')

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, t):
        self.__telefone = t

    @property
    def biografia(self):
        return self.__biografia

    @biografia.setter
    def biografia(self, bio):
        self.__biografia = bio


def organiza_categoria():
    print(menu_categoria)
    opcao_categoria = input('Digite a opção: ')
    if opcao_categoria == '0':
        return
    elif opcao_categoria == '1':
        if tabela_categorias == []:
            print('Não existem categorias cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            print('ID | Nome')
            for index, categoria in enumerate(tabela_categorias):
                print(f"{index + 1} | {categoria['nome']}")
            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_categoria == '2':
        nome_categoria = input('Digite o nome da categoria: ')
        nova_categoria = {
            'nome': nome_categoria
        }
        tabela_categorias.append(nova_categoria)
        print('Categoria cadastrada com sucesso!')
        input('\nPressione <ENTER> para continuar...\n')
    elif opcao_categoria == '3':
        if tabela_categorias == []:
            print('Não existem categorias cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_categoria = int(input('Digite o ID da categoria a ser excluída: '))
                tabela_categorias.pop(id_categoria - 1)
                print('Categoria excluída com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_categoria == '4':
        if tabela_categorias == []:
            print('Não existem categorias cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_categoria = int(input('Digite o ID do categoria a ser consultada: '))
                categoria = tabela_categorias[id_categoria - 1]
                print('ID | Nome')
                print(f"{id_categoria} | {categoria['nome']}")
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_categoria == '5':
        if tabela_categorias == []:
            print('Não existem categorias cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_categoria = int(input('Digite o ID da categoria a ser editada: '))
                categoria = tabela_categorias[id_categoria - 1]

                nome_categoria = input('Digite o nome da categoria: ')

                categoria['nome'] = nome_categoria

                print('Categoria editada com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    else:
        print('Opção inválida!')
        input()

    organiza_categoria()

def organiza_editora():
    print(menu_editora)
    opcao_editora = input('Digite a opção: ')
    if opcao_editora == '0':
        return
    elif opcao_editora == '1':
        if tabela_editoras == []:
            print('Não existem editoras cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            print('ID | Nome | Endereço | Telefone')
            for index, editora in enumerate(tabela_editoras):
                print(f"{index + 1} | {editora['nome']} | {editora['endereco']} | {editora['telefone']}")

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_editora == '2':
        nome_editora = input('Digite o nome da editora: ')
        endereco_editora = input('Digite o endereço da editora: ')
        telefone_editora = input('Digite o telefone da editora: ')
        nova_editora = {
            'nome': nome_editora,
            'endereco': endereco_editora,
            'telefone': telefone_editora
        }
        tabela_editoras.append(nova_editora)
        print('Editora cadastrada com sucesso!')
        input('\nPressione <ENTER> para continuar...\n')
    elif opcao_editora == '3':
        if tabela_editoras == []:
            print('Não existem editoras cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_editora = int(input('Digite o ID da editora a ser excluída: '))
                tabela_editoras.pop(id_editora - 1)
                print('Editora excluída com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_editora == '4':
        if tabela_editoras == []:
            print('Não existem editoras cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_editora = int(input('Digite o ID da editora a ser consultada: '))
                editora = tabela_editoras[id_editora - 1]
                print('ID | Nome | Endereço | Telefone')
                print(f"{id_editora} | {editora['nome']} | {editora['endereco']} | {editora['telefone']}")
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_editora == '5':
        if tabela_editoras == []:
            print('Não existem editoras cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_editora = int(input('Digite o ID da editora a ser editada: '))
                editora = tabela_editoras[id_editora - 1]

                nome_editora = input('Digite o nome da editora: ')
                endereco_editora = input('Digite o endereço da editora: ')
                telefone_editora = input('Digite o telefone da editora: ')

                editora['nome'] = nome_editora
                editora['endereco'] = endereco_editora
                editora['telefone'] = telefone_editora

                print('Editora editada com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    else:
        print('Opção inválida!')
        input()

    organiza_editora()

def organiza_autor():
    print(menu_autor)
    opcao_autor = input('Digite a opção: ')
    if opcao_autor == '0':
        return
    elif opcao_autor == '1':
        if tabela_autores == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            print('ID | Nome | E-mail | Telefone | Biografia')
            for index, autor in enumerate(tabela_autores):
                print(f"{index + 1} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.biografia}")

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_autor == '2':
        nome_autor = input('Digite o nome do autor: ')
        telefone_autor = input('Digite o telefone do autor: ')
        bio_autor = input('Digite a biografia do autor: ')

        while True:
            try:
                email_autor = input('Digite o e-mail do autor: ')
                novo_autor = Autor(nome_autor, email_autor, telefone_autor, bio_autor)
                break
            except Exception as ex:
                print(f'Ocorreu um erro: {ex}')

        tabela_autores.append(novo_autor)
        print('Autor cadastrado com sucesso!')
        input('\nPressione <ENTER> para continuar...\n')
    elif opcao_autor == '3':
        if tabela_autores == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser excluído: '))
                tabela_autores.pop(id_autor - 1)
                print('Autor excluído com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_autor == '4':
        if tabela_autores == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser consultado: '))
                autor = tabela_autores[id_autor - 1]
                print('ID | Nome | E-mail | Telefone | Biografia')
                print(f"{id_autor} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.biografia}")
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    elif opcao_autor == '5':
        if tabela_autores == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser editado: '))
                autor = tabela_autores[id_autor - 1]

                nome_autor = input('Digite o nome do autor: ')
                telefone_autor = input('Digite o telefone do autor: ')
                bio_autor = input('Digite a biografia do autor: ')

                autor.nome = nome_autor
                autor.telefone = telefone_autor
                autor.biografia = bio_autor
                while True:
                    try:
                        email_autor = input('Digite o e-mail do autor: ')
                        autor.email = email_autor
                        break
                    except Exception as ex:
                        print(f'Ocorreu um erro: {ex}')

                print('Autor editado com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')
    else:
        print('Opção inválida!')
        input()

    organiza_autor()

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

    if op == '0':
        break
    elif op == '1':
        organiza_categoria()
    elif op == '2': # else if
        organiza_editora()
    elif op == '3':
        organiza_autor()
    elif op == '4':
        organiza_livro()
    else:
        print('Opção inválida!')
        input()

print('Programa encerrado!')

