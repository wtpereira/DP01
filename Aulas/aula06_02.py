def saudacoes(nome1):
    print(f'Olá, {nome1}!')


def pega_sobrenome(nome2):
    sobrenome = input(f'Por favor {nome2}, digite o seu sobrenome: ')
    print(f'{nome2} {sobrenome}')


nome = input('Digite o seu nome: ')
saudacoes(nome)
pega_sobrenome(nome)

