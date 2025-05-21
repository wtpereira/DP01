def email_valido(email):
    if email.find('@') >= 1 and email.find('.com') >= 3:
        return True
    else:
        return False


class Autor:
    def __init__(self, n, e, t, b):  # construtor ou inicializador
        print('Estou no construtor!')
        self.nome = n.title()
        self.email = e
        self.telefone = t
        self.biografia = b

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

try:
    novo_autor = Autor('machado de assis', 'TESTE@M.com', 123, 'biom')
    print(novo_autor.nome)
    print(novo_autor.email)
    print(novo_autor.telefone)
    print(novo_autor.biografia)

    novo_autor.email = 'xxx@teste.com'
    print(novo_autor.email)
except Exception as ex:
    print(f'Ocorreu um erro ao instanciar um novo autor: {ex}')

