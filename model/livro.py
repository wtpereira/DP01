class Livro:
    id_livro = 1

    def __init__(self, titulo: str, resumo: str, ano: int, paginas: int, isbn: str):
        self.id = Livro.id_livro
        self.titulo = titulo
        self.resumo = resumo
        self.ano = ano
        self.paginas = paginas
        self.isbn = isbn

    def __str__(self):
        return f"{self.id} | {self.titulo} | {self.ano} | {self.paginas} | {self.isbn} | {self.resumo} | {self.autor.nome} | {self.categoria.nome} | {self.editora.nome}"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
        Livro.id_livro += 1

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo.title()

    @property
    def resumo(self):
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo):
        self.__resumo = resumo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def paginas(self):
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas):
        self.__paginas = paginas

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora
