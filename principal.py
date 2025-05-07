menu_principal = """[Menu Principal] Escolha uma das seguintes opções:
1 - Categorias
2 - Editoras
3 - Autores
4 - Livros
0 - Sair do programa"""

print(menu_principal)

while True:
    op = input('Digite a opção: ')

    if op == '0':
        break
    elif op == '1':
        print('Opção escolhida: Categorias')
        input('Digite <ENTER> para continuar...')
    elif op == '2': # else if
        print('Opção escolhida: Editoras')
        input('Digite <ENTER> para continuar...')
    elif op == '3':
        print('Opção escolhida: Autores')
        input('Digite <ENTER> para continuar...')
    elif op == '4':
        print('Opção escolhida: Livros')
        input('Digite <ENTER> para continuar...')
    else:
        print('Opção inválida!')

print('Programa encerrado!')

