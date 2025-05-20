class Autor:
    def __init__(self):  # construtor ou inicializador
        print('Estou no construtor!')
        self.nome = None
        self.email = None
        self.telefone = None
        self.biografia = None


novo_autor = Autor()  # Criar uma nova instância (instanciar) de Autor

print(novo_autor)
