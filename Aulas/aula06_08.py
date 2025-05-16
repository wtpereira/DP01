def soma_multiplicada_dividida(*args, m=1, d=1):  # é a forma de definir um valor padrão para o parâmetro 'm'.
    resultado = 0
    for elemento in args:
        resultado += elemento

    return resultado * m



print(f'O resultado da soma multiplicada é: {soma_multiplicada_dividida(4, 8, 12, 16, 20, 24, 28, 32, m=3, d=5)}')
print(f'O resultado da soma multiplicada é: {soma_multiplicada_dividida(4, 8, 12, 16, 20, 24, 28, 32, d=5, m=3)}')