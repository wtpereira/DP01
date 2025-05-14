print('Início do programa!')

lista = [1, 2, 3, 4]

id = int(input('Digite o ID: '))


while True:
    if id >= 1 and id <= len(lista):
        print(lista[id - 1])
    else:
        print('ID não encontrado.')

    id = int(input('Digite um ID válido: '))


print('Fim do programa!')