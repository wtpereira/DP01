class Aluno:
    def __init__(self, nome):  # dunder (double under) init
        self.nome = nome

    def __str__(self):  # dunder str
        return f'Nome do Aluno: {self.nome}'

    def __repr__(self): # dunder repr
        return f'Aluno("{self.nome}")'


aluno = Aluno('Well')
print(aluno)
