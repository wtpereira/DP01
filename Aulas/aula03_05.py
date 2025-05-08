# Exibir a tabuada do número inteiro positivo digitado pelo usuário no intervalo de zero a dez (usando while)

numero = int(input('Digite um número inteiro positivo: '))

while numero < 1:
    numero = int(input('Digite um número inteiro positivo: '))

index = 0
while index <= 10:
    print(f'5 x {index} = {5 * index}')
    index += 1

