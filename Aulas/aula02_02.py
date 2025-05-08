numeros = []


for i in range(0, 10, 1):
    n = input(f'Digite o {i + 1}º valor: ')
    numeros.append(n)

for j in range(9, -1, -1):
    print(numeros[j])
