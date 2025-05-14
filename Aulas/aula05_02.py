print('Início do programa!')
lista = ['um', 'dois', 'três', 'quatro']

try:
    id = input('Digite o ID: ')
    id = int(id)
    print(lista[id - 1])
    print(1/0)  # Erro inserido para efeito didático.
except ValueError as ex:
    print('Erro de conversão.')
except IndexError as ex:
    print('Índice não encontrado.')
except Exception as ex:
    print(f'Ocorreu um erro inesperado: {ex}')

print('Fim do programa!')