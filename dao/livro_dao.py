class LivroDAO:
    tabela_livros = []

    def listar(self):
        return LivroDAO.tabela_livros

    def adicionar(self, novo_livro):
        LivroDAO.tabela_livros.append(novo_livro)

    def remover(self, id_livro):
        for index, livro in enumerate(LivroDAO.tabela_livros):
            if livro.id == id_livro:
                LivroDAO.tabela_livros.pop(index)
                return True

        return False

    def buscar_por_id(self, id_livro):
        for livro in LivroDAO.tabela_livros:
            if livro.id == id_livro:
                return livro

        return None

    def editar(self, id_livro):
        pass
