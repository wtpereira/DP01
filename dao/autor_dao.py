from model.autor import Autor


class AutorDAO:
    tabela_autores = []

    def listar(self):
        if AutorDAO.tabela_autores == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            print('ID | Nome | E-mail | Telefone | Biografia')
            for index, autor in enumerate(AutorDAO.tabela_autores):
                print(f"{index + 1} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.biografia}")

            input('\nPressione <ENTER> para continuar...\n')

    def adicionar(self):
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

        AutorDAO.tabela_autores.append(novo_autor)
        print('Autor cadastrado com sucesso!')
        input('\nPressione <ENTER> para continuar...\n')

    def remover(self):
        if AutorDAO.tabela_autores == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser excluído: '))
                AutorDAO.tabela_autores.pop(id_autor - 1)
                print('Autor excluído com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')

    def buscar_por_id(self):
        if AutorDAO.tabela_autores == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser consultado: '))
                autor = AutorDAO.tabela_autores[id_autor - 1]
                print('ID | Nome | E-mail | Telefone | Biografia')
                print(f"{id_autor} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.biografia}")
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')

    def editar(self):
        if AutorDAO.tabela_autores == []:
            print('Não existem autores cadastrados.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_autor = int(input('Digite o ID do autor a ser editado: '))
                autor = AutorDAO.tabela_autores[id_autor - 1]

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