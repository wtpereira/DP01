from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria


menu_categorias = """
\033[44m[Categorias] Escolha uma das seguintes opções:\033[0m
1 - Listar toda as categorias
2 - Adicionar nova categoria
3 - Excluir categoria
4 - Ver categoria por Id
0 - Voltar ao menu anterior
"""


class CategoriaService:
    categoria_dao: CategoriaDAO = CategoriaDAO()

    def menu(self):
        print(menu_categorias)
        escolha = input('Digite a opção: ')

        if escolha == '0':
            return
        elif escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida. Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('Listando categorias...')

        try:
            categorias = CategoriaService.categoria_dao.listar()
        except Exception as e:
            print(f'Erro ao exibir as categorias! - {e}')
        else:
            if categorias:
                print('Id | Nome')
                for categoria in categorias:
                    print(categoria)
            else:
                print('Nenhuma categoria encontrada!')

    def adicionar(self):
        print('\nAdicionando categoria...')
        nome = input('Digite o nome da categoria de livro: ')
        nova_categoria = Categoria(nome)
        try:
            CategoriaService.categoria_dao.adicionar(nova_categoria)
        except Exception as e:
            print(f'Erro ao adicionar categoria! - {e}')
        else:
            print('Categoria adicionada com sucesso!')

    def remover(self):
        if CategoriaService.categoria_dao.listar() == []:
            print("Nenhuma Categoria cadastrada.")
            input("Pressione <ENTER> para continuar.")
            return

        print('Removendo categoria...')
        categoria_id = int(input('Digite o ID da categoria para excluir: '))
        if CategoriaService.categoria_dao.remover(categoria_id):
            print('Categoria excluída com sucesso!')
        else:
            print('Categoria não encontrada!')

    def mostrar_por_id(self):
        if CategoriaService.categoria_dao.listar() == []:
            print("Nenhuma Categoria cadastrada.")
            input("Pressione <ENTER> para continuar.")
        else:
            print('Mostrar categoria por ID...')
            try:
                categoria_id = int(input('Digite o ID da categoria para buscar: '))
                categoria = CategoriaService.categoria_dao.buscar_por_id(categoria_id)
                if categoria:
                    print('Id | Nome')
                    print(categoria)
                else:
                    print('Categoria não encontrada!')
            except Exception as ex:
                print(f'Erro ao exibir categoria por ID: {ex}')
