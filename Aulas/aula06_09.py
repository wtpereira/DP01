def soma_multiplicada_n_vezes(*args, **kwargs):  # é a forma de definir um valor padrão para o parâmetro 'm'.
    resultado = 0
    for elemento in args:
        resultado += elemento

    for chave, multiplicador in kwargs.items():
        # print(f'chave = {chave}, multiplicador = {multiplicador}')
        resultado *= multiplicador

    return resultado

resp = soma_multiplicada_n_vezes(1, 2, 3, m1=4)
print(f'O resultado é: {resp}')

resp = soma_multiplicada_n_vezes(1, 2, 3, m1=4, m2=10)
print(f'O resultado é: {resp}')

resp = soma_multiplicada_n_vezes(1, 2, 3, m1=4, m2=10, m3=20)
print(f'O resultado é: {resp}')

