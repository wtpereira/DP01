class Aluno:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


if __name__ == '__main__':
    aluno = Aluno('João', 'Silva')
    print(aluno.nome)
    print(aluno.sobrenome)

