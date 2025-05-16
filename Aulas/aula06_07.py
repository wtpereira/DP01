def soma_multiplicada11(a, b, c, d):
    return (a + b + c + d) * 11

def soma_multiplicada15(a, b, c, d):
    return (a + b + c + d) * 15

print(f'O resultado da soma multiplicada é: {soma_multiplicada11(3, 5, 7, 9)}')
print(f'O resultado da soma multiplicada é: {soma_multiplicada15(11, 24, 1, 3)}')


def soma_multiplicada(a, b, c, d, m):
    return (a + b + c + d) * m

print(f'O resultado da soma multiplicada é: {soma_multiplicada(3, 5, 7, 9, 11)}')
print(f'O resultado da soma multiplicada é: {soma_multiplicada(11, 24, 1, 3, 15)}')


# Redefinindo a função.
def soma_multiplicada(*args, m):
    resultado = 0
    for elemento in args:
        resultado += elemento

    return resultado * m


print(f'O resultado da soma multiplicada é: {soma_multiplicada(3, 5, 7, 9, m=11)}')
print(f'O resultado da soma multiplicada é: {soma_multiplicada(11, 24, 1, 3, m=15)}')

print(f'O resultado da soma multiplicada é: {soma_multiplicada(4, 8, 12, 16, 20, 24, 28, 32, m=3)}')

print(f'O resultado da soma multiplicada é: {soma_multiplicada(3, m=3)}')

print(f'O resultado da soma multiplicada é: {soma_multiplicada(m=3)}')


# Redefinindo a função.
def soma_multiplicada(*args, m=1):  # é a forma de definir um valor padrão para o parâmetro 'm'.
    resultado = 0
    for elemento in args:
        resultado += elemento

    return resultado * m

print(f'O resultado da soma multiplicada é: {soma_multiplicada(3)}')

