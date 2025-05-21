from dao.autor_dao import AutorDAO

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
        AutorService.autor_dao.listar()

    def adicionar(self):
        AutorService.autor_dao.adicionar()

    def remover(self):
        pass

    def mostrar_por_id(self):
        pass

    def editar(self):
        pass