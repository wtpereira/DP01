def email_valido(email):
    if email.find('@') >= 1 and email.find('.com') >= 3:
        return True
    else:
        return False


class Autor:
    __slots__ = ['__nome', '__email', '__telefone', '__biografia']

    def __init__(self, n, e, t, b):  # construtor ou inicializador
        print('Estou no construtor!')
        self.nome = n
        self.email = e
        self.telefone = t
        self.biografia = b

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
            raise Exception('E-mail inválido')

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


autor = Autor('Machado', 'm@m.com', 123, 'biom')

print(autor)
print(autor.email)

print(autor._Autor__email)

