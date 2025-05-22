from dao.autor_dao import AutorDAO
from model.autor import Autor

menu_autor = """
[Autores] Escolha uma das seguintes opções:
1 - Listar todos os autores
2 - Adicionar novo autor
3 - Excluir autor
4 - Ver autor por Id
5 - Editar autor
0 - Voltar ao menu anterior
"""

class AutorService:
    autor_dao = AutorDAO()

    def menu(self):
        print(menu_autor)
        opcao_autor = input('Digite a opção: ')
        if opcao_autor == '0':
            return
        elif opcao_autor == '1':
            self.listar()
        elif opcao_autor == '2':
            self.adicionar()
        elif opcao_autor == '3':
            self.remover()
        elif opcao_autor == '4':
            self.mostrar_por_id()
        elif opcao_autor == '5':
            self.editar()
        else:
            print('Opção inválida!')
            input()

        self.menu()

    def listar(self):
        if AutorService.autor_dao.listar() == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            print('ID | Nome | E-mail | Telefone | Biografia')
            for index, autor in enumerate(AutorService.autor_dao.listar()):
                print(f"{autor.id} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.biografia}")

            input('\nPressione <ENTER> para continuar...\n')

    def adicionar(self):
        nome_autor = input('Digite o nome do autor: ')
        telefone_autor = input('Digite o telefone do autor: ')
        bio_autor = input('Digite a biografia do autor: ')
        while True:
            try:
                email_autor = input('Digite o e-mail do autor: ')
                novo_autor = Autor(nome_autor, email_autor, telefone_autor, bio_autor)
            except Exception as ex:
                print(f'Ocorreu um erro: {ex}')
            else:  # Caso não ocorra nenhuma exceção
                AutorService.autor_dao.adicionar(novo_autor)
                print('Autor cadastrado com sucesso!')
                break  # encerrar o 'while'

        input('\nPressione <ENTER> para continuar...\n')

    def remover(self):
        if AutorService.autor_dao.listar() == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            id_autor = int(input('Digite o ID do autor a ser excluído: '))
            if AutorService.autor_dao.remover(id_autor):
                print('Autor excluído com sucesso!')
            else:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')

    def mostrar_por_id(self):
        if AutorService.autor_dao.listar() == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser consultado: '))
                autor = AutorService.autor_dao.buscar_por_id(id_autor)
                if autor:
                    print('ID | Nome | E-mail | Telefone | Biografia')
                    print(f"{autor.id} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.biografia}")
                else:
                    print('ID não encontrado.')
            except Exception as ex:
                print(f'ID inválido: {ex}.')

            input('\nPressione <ENTER> para continuar...\n')

    def editar(self):
        if AutorService.autor_dao.listar() == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser editado: '))
                autor = AutorService.autor_dao.editar(id_autor)
                if autor:
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
                        else:
                            print('Autor editado com sucesso!')
                else:
                    print('ID não encontrado.')
            except Exception as ex:
                print(f'ID inválido: {ex}.')

            input('\nPressione <ENTER> para continuar...\n')