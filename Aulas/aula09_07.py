def add100(n):
    return n + 100

resultado = add100(40)
print(f'O resultado é: {resultado}')

print('*' * 80)

add100 = lambda n: n + 100

resp = add100(40)
print(f'O resultado é: {resp}')
