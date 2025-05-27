from dao.editora_dao import EditoraDAO
from model.editora import Editora


menu_editoras = """
\033[44m[Editoras] Escolha uma das seguintes opções:\033[0m
1 - Listar todas as editoras
2 - Adicionar nova editora
3 - Excluir editora
4 - Ver editora por Id
0 - Voltar ao menu anterior
"""


class EditoraService:
    editora_dao: EditoraDAO = EditoraDAO()

    def menu(self):
        print(menu_editoras)
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
        print('\nListando editoras...')

        try:
            editoras = EditoraService.editora_dao.listar()
            if editoras:
                print('Id | Nome | Endereço | Telefone')
                for editora in editoras:
                    print(editora)
            else:
                print('Nenhuma editora encontrada!')
        except Exception as e:
            print(f'Erro ao exibir as editoras! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando editora...')

        nome = input('Digite o nome da editora: ')
        endereco = input('Digite o endereço da editora: ')
        telefone = input('Digite o telefone da editora: ')
        nova_editora = Editora(nome, endereco, telefone)
        try:
            EditoraService.editora_dao.adicionar(nova_editora)
        except Exception as e:
            print(f'Erro ao inserir editora! - {e}')
        else:
            print('Editora adicionada com sucesso!')

        input('Pressione uma tecla para continuar...')

    def remover(self):
        if EditoraService.autor_dao.listar() == []:
            print("Nenhuma Editora cadastrada.")
            input("Pressione <ENTER> para continuar.")
            return

        print('\nRemovendo editora...')

        try:
            editora_id = int(input('Digite o ID da excluir para excluir: '))
            if (EditoraService.editora_dao.remover(editora_id)):
                print('Editora excluída com sucesso!')
            else:
                print('Editora não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir editora! - {e}')
            return

    def mostrar_por_id(self):
        if EditoraService.autor_dao.listar() == []:
            print("Nenhuma Editora cadastrada.")
            input("Pressione <ENTER> para continuar.")
        else:
            print('\nEditora por Id...')

            try:
                id = int(input('Digite o Id da editora para buscar: '))
                edt = EditoraService.editora_dao.buscar_por_id(id)
                if edt:
                    print('Id | Nome | Endereço | Telefone')
                    print(edt)
                else:
                    print('Editora não encontrada!')
            except Exception as e:
                print(f'Erro ao exibir editora! - {e}')
                return

    def editar(self):
        if EditoraService.autor_dao.listar() == []:
            print('Não existem editoras cadastradas.')
            input('\nPressione <ENTER> para continuar...\n')
        else:
            try:
                id_editora = int(input('Digite o ID da editora a ser editada: '))
                editora = EditoraService.editora_dao.buscar_por_id(id)

                nome_editora = input('Digite o nome da editora: ')
                endereco_editora = input('Digite o endereço da editora: ')
                telefone_editora = input('Digite o telefone da editora: ')

                editora.nome = nome_editora
                editora.endereco = endereco_editora
                editora.telefone = telefone_editora

                print('Editora editada com sucesso!')
            except:
                print('ID inválido ou não encontrado.')

            input('\nPressione <ENTER> para continuar...\n')