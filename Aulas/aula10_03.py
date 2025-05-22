def fn(valor):
    if valor == 'a':
        print('Letra A')
    elif valor == 'b':
        print('Letra B')
    else:
        print('Qualquer outra letra.')

fn('b')

def fn(valor):
    match valor:
        case 'a':
            print('Letra A')
        case 'b':
            print('Letra B')
        case _:
            print('Qualquer outra letra.')

fn('c')

print('*' * 40)

def fn(valor):
    if valor < 10:
        print('Menor que 10')
    elif valor < 20:
        print('Maior ou igual a 10 e menor que 20')
    else:
        print('Maior ou igual a 20')

fn(5)
fn(14)
fn(50)

print('*' * 40)

def fnmc(valor):
    match valor:
        case _ if valor < 10:
            print('Menor que 10')
        case _ if valor < 20:
            print('Maior ou igual a 10 e menor que 20')
        case _:
            print('Maior ou igual a 20')

fnmc(9)
fnmc(10)
fnmc(20)
