from model.utils import email_valido


class Autor:
    id_autor = 1
    __slots__ = ['__id', '__nome', '__email', '__telefone', '__biografia']

    def __init__(self, n: str, e: str, t: str, b: str):  # construtor ou inicializador
        self.id = Autor.id_autor
        self.nome = n
        self.email = e
        self.telefone = t
        self.biografia = b

    def __str__(self) -> str:
        return f"{self.id} | {self.nome} | {self.email} | {self.telefone} | {self.biografia}"

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, i: int):
        self.__id = i
        Autor.id_autor += 1

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, n: str):
        self.__nome = n.title()

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, e: str):
        e = e.lower()  # Transformar para minúsculo.
        if email_valido(e):
            self.__email = e
            return
        else:
            self.__email = None
            raise Exception('E-mail inválido!')

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, t: str):
        self.__telefone = t

    @property
    def biografia(self) -> str:
        return self.__biografia

    @biografia.setter
    def biografia(self, bio: str):
        self.__biografia = bio

