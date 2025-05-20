def email_valido(email):
    if email.find('@') >= 1 and email.find('.com') >= 3:
        return True
    else:
        return False


class Autor:
    def __init__(self, n, e, t, b):  # construtor ou inicializador
        print('Estou no construtor!')
        self.nome = n
        self.email = e
        self.telefone = t
        self.biografia = b


novo_autor = Autor('Machado', 'm@m.com', 123, 'biom')
if email_valido(novo_autor.email):
    print('Email válido!')
else:
    print('Email inválido!!!')
