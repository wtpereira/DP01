def email_valido(email):
    if email.find('@') >= 1 and email.find('.com') >= 3:
        return True
    else:
        return False


class Autor:
    def __init__(self, n, e, t, b):  # construtor ou inicializador
        print('Estou no construtor!')
        self.nome = n
        self.set_email(e)
        self.telefone = t
        self.biografia = b

    # getter
    def get_email(self):
        return self.email

    # setter
    def set_email(self, e):
        self.email = e.lower()

novo_autor = Autor('Machado', 'TESTE@M', 123, 'biom')

print(novo_autor.email)

