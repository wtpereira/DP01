class LivroDAO:
    tabela_livros = []

    def listar(self):
        return LivroDAO.tabela_livros

    def adicionar(self, novo_livro):
        LivroDAO.tabela_livros.append(novo_livro)

    def remover(self, id_livro):
        pass

    def buscar_por_id(self, id_livro):
        pass

    def editar(self, id_livro):
        pass
