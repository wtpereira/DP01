class Autor:
    def __init__(self):  # construtor ou inicializador
        print('Estou no construtor!')
        self.nome = None
        self.email = None
        self.telefone = None
        self.biografia = None


novo_autor = Autor()  # Criar uma nova instância (instanciar) de Autor

print(novo_autor)
print(f'Nome do autor: {novo_autor.nome}')
print(f'E-mail do autor: {novo_autor.email}')
print(f'Telefone do autor: {novo_autor.telefone}')
print(f'Biografia do autor: {novo_autor.biografia}')

