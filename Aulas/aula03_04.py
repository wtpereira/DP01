# Exibir a tabuada do número inteiro positivo digitado pelo usuário no intervalo de zero a dez (usando for)

numero = int(input('Digite um número inteiro positivo: '))

while numero < 1:
    numero = int(input('Digite um número inteiro positivo: '))

for index in range(11):
    print(f'{numero} x {index} = {numero * index}')

