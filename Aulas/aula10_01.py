class Teste:
    atributo_teste = ['a', 'b', 'c']

    def __init__(self):
        self.atributo_teste =[1, 2, 3]


print(Teste.atributo_teste)

teste = Teste()
print(teste.atributo_teste)

print(Teste.atributo_teste)