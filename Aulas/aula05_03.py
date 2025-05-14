def minha_funcao():
    a = int(input('Entre com o primeiro número: '))
    b = int(input('Entre com o segundo número: '))

    print(f'O Resultado da soma é {a + b}')

op = ''
while op != 'n':
    minha_funcao()
    op = input('Deseja continuar (S/n): ')

print('\nVárias linhas de código.\n')

op = ''
while op != 'n':
    minha_funcao()
    op = input('Deseja continuar (S/n): ')

