class Autor:
    def __init__(self):  # construtor ou inicializador
        print('Estou no construtor!')
        self.nome = 'Cecília'
        self.email = 'cecilia@teste'
        self.telefone = 1234
        self.biografia = 'biocccc'


novo_autor = Autor()  # Criar uma nova instância (instanciar) de Autor

print(novo_autor)
print(f'Nome do autor: {novo_autor.nome}')
print(f'E-mail do autor: {novo_autor.email}')
print(f'Telefone do autor: {novo_autor.telefone}')
print(f'Biografia do autor: {novo_autor.biografia}')

outro_autor = Autor()
print(outro_autor)
print(f'Nome do autor: {outro_autor.nome}')
print(f'E-mail do autor: {outro_autor.email}')
print(f'Telefone do autor: {outro_autor.telefone}')
print(f'Biografia do autor: {outro_autor.biografia}')
