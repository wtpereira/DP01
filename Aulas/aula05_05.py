def minha_funcao():
    a = int(input('Entre com o primeiro número: '))
    b = int(input('Entre com o segundo número: '))

    print(f'O resultado da multiplicação é: {a * b}')
    if b == 0:
        return

    print(f'O resultado da divisão é: {a / b}')


def loop():
    print('Início do loop()')
    while True:
        minha_funcao()
        op = input('Deseja continuar (S/n): ')
        if op == 'n':
            return
        print()

    print('Fim do loop()')


loop()
print('Fim do programa!')