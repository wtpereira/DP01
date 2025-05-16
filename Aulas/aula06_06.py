def soma2(a, b):
    return a + b

def soma3(a, b, c):
    return a + b + c

def soma4(a, b, c, d):
    return a + b + c + d


print(f'O resultado da soma é {soma2(10, 3)}')

print(f'O resultado da soma é {soma2(254, 89)}')

print(f'O resultado da soma é {soma3(15, 17, 19)}')

print(f'O resultado da soma é {soma4(105, 171, 319, 3)}')


def soma(*args):
    resultado = 0
    for elemento in args:
        resultado += elemento

    return resultado

print(f'O resultado da soma é {soma(3, 4)}')
print(f'O resultado da soma é {soma(3, 4, 5)}')
print(f'O resultado da soma é {soma(3, 4, 5, 16)}')
print(f'O resultado da soma é {soma(3, 4, 5, 16, 987)}')
