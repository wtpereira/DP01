from model.autor import Autor


class AutorDAO:
    tabela_autores = []

    def listar(self):
        return AutorDAO.tabela_autores

    def adicionar(self, novo_autor):
        AutorDAO.tabela_autores.append(novo_autor)

    def remover(self, id_autor):
        for index, autor in enumerate(AutorDAO.tabela_autores):
            if autor.id == id_autor:
                AutorDAO.tabela_autores.pop(index)
                return True

        return False

    def buscar_por_id(self, id_autor):
        for autor in AutorDAO.tabela_autores:
            if autor.id == id_autor:
                return autor

        return None

    def editar(self, id_autor):
        for autor in AutorDAO.tabela_autores:
            if autor.id == id_autor:
                return autor

        return None