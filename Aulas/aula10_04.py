def add(a, b):
    return a + b


print(f'O resultado é: {add(10, 5)}')
print(f'O resultado é: {add('abc', 'def')}')
# print(f'O resultado é: {add('abc', 10)}')  # vai dar erro


def multiply(x: int, y: int) -> int:
    print(f'Primeiro valor: {x}')
    print(f'Segundo valor: {y}')
    return x * y


print(f'O resultado é: {multiply(10, 5)}')
# print(f'O resultado é: {multiply('abc', 'def')}')  # vai dar erro


def imprime_linha(c: str, x: int) -> str:
    return c * x

print(imprime_linha('-', 80))

