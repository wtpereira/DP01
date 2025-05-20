class Autor:
    def __init__(self, n, e, t, b):  # construtor ou inicializador
        print('Estou no construtor!')
        self.nome = n
        self.email = e
        self.telefone = t
        self.biografia = b

novo_autor = Autor('Machado', 'm@m', 123, 'biom')

print(novo_autor)
print(f'Nome do autor: {novo_autor.nome}')
print(f'E-mail do autor: {novo_autor.email}')
print(f'Telefone do autor: {novo_autor.telefone}')
print(f'Biografia do autor: {novo_autor.biografia}')

print()

outro_autor = Autor('José Saramago', 'j@s', 665, 'biojs')
print(outro_autor)
print(f'Nome do autor: {outro_autor.nome}')
print(f'E-mail do autor: {outro_autor.email}')
print(f'Telefone do autor: {outro_autor.telefone}')
print(f'Biografia do autor: {outro_autor.biografia}')