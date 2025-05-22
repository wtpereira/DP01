from model.utils import email_valido


class Autor:
    id_autor = 1
    __slots__ = ['__id', '__nome', '__email', '__telefone', '__biografia']

    def __init__(self, n, e, t, b):  # construtor ou inicializador
        self.id = Autor.id_autor
        self.nome = n
        self.email = e
        self.telefone = t
        self.biografia = b

    def __str__(self):
        return f"{self.id} | {self.nome} | {self.email} | {self.telefone} | {self.biografia}"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, i):
        self.__id = i
        Autor.id_autor += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        self.__nome = n.title()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, e):
        e = e.lower()  # Transformar para minúsculo.
        if email_valido(e):
            self.__email = e
            return
        else:
            self.__email = None
            raise Exception('E-mail inválido!')

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, t):
        self.__telefone = t

    @property
    def biografia(self):
        return self.__biografia

    @biografia.setter
    def biografia(self, bio):
        self.__biografia = bio

