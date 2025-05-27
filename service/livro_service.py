from dao.livro_dao import LivroDAO
from model.livro import Livro
from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService

menu_livro = """
\033[0;34m[Livros] Escolha uma das seguintes opções:\033[0m
1 - Listar todos os livros
2 - Adicionar novo livro
3 - Excluir livro
4 - Ver livro por Id
5 - Editar livro
0 - Voltar ao menu anterior
"""


class LivroService:
    livro_dao = LivroDAO()
    autor_service = AutorService()
    categoria_service = CategoriaService()
    editora_service = EditoraService()

    def menu(self):
        print(menu_livro)
        opcao_livro = input('Digite a opção: ')
        match opcao_livro:
            case '0':
                return
            case '1':
                self.listar()
            case '2':
                self.adicionar()
            case '3':
                self.remover()
            case '4':
                self.mostrar_por_id()
            case '5':
                self.editar()
            case _:
                print('Opção inválida!')
                input()

        self.menu()

    def listar(self):
        if not LivroService.livro_dao.listar():
            print('Não existem livros cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            print('ID | Título | Ano | Qtde páginas | ISBN | Resumo | Autor | Categoria | Editora')
            for index, livro in enumerate(LivroService.livro_dao.listar()):
                print(livro)

            input('\nPressione <ENTER> para continuar...\n')

    def adicionar(self):
        if LivroService.autor_service.autor_dao.listar() == [] or LivroService.categoria_service.categoria_dao.listar() == [] or LivroService.editora_service.editora_dao.listar() == []:
            print('É necessário pelo menos um autor, uma categoria, e uma editora cadastros.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            titulo = input('Digite o título do livro: ')
            resumo = input('Digite o resumo do livro: ')
            ano = input('Digite o ano de publicação do livro: ')
            paginas = input('Digite a quantidade de páginas: ')
            isbn = input('Digite o ISBN do livro: ')
            novo_livro = Livro(titulo, resumo, ano, paginas, isbn)

            while True:
                id_autor = int(input('Digite o ID do autor: '))
                autor = LivroService.autor_service.autor_dao.buscar_por_id(id_autor)
                if autor:
                    novo_livro.autor = autor
                    break
                else:
                    print('ID de autor não encontrado.')

            while True:
                id_categoria = int(input('Digite o ID da categoria: '))
                categoria = LivroService.categoria_service.categoria_dao.buscar_por_id(id_categoria)
                if categoria:
                    novo_livro.categoria = categoria
                    break
                else:
                    print('ID de categoria não encontrado.')

            while True:
                id_editora = int(input('Digite o ID da editora: '))
                editora = LivroService.editora_service.editora_dao.buscar_por_id(id_editora)
                if editora:
                    novo_livro.editora = editora
                    break
                else:
                    print('ID de editora não encontrado.')

            LivroService.livro_dao.adicionar(novo_livro)
            print('Livro cadastrado com sucesso!')
            input('\nPressione <ENTER> para continuar...\n')

    def remover(self):
        pass
    def mostrar_por_id(self):
        pass
    def editar(self):
        pass
