class Teste:
    atributo_teste = ['a', 'b', 'c']

    def __init__(self):
        self.atributo_teste = self.atributo_teste.pop(1)  # o ideal seria: Teste.atributo_teste.pop(1)

print(Teste.atributo_teste)

teste = Teste()
print(teste.atributo_teste)

print(Teste.atributo_teste)