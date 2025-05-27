from model.categoria import Categoria

class CategoriaDAO:
    tabela_categorias = []

    def listar(self) -> list:  # SELECT * FROM categoria
        return CategoriaDAO.tabela_categorias

    def adicionar(self, categoria: Categoria) -> None:  # INSERT INTO categoria
        CategoriaDAO.tabela_categorias.append(categoria)

    def remover(self, categoria_id: int) -> bool:
        encontrado = False

        for index, categoria in enumerate(CategoriaDAO.tabela_categorias):
            if categoria.id == categoria_id:
                encontrado = True
                break

        if encontrado:
            CategoriaDAO.tabela_categorias.pop(index)

        return encontrado

    def buscar_por_id(self, categoria_id) -> Categoria:
        for categoria in CategoriaDAO.tabela_categorias:
            if categoria.id == categoria_id:
                return categoria
