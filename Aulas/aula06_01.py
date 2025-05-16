def minha_funcao():
    a = int(input('Entre com o primeiro número: '))
    b = int(input('Entre com o segundo número: '))

    print(f'O Resultado da soma é {a + b}')

minha_funcao()

# A função acima será ignorada por causa da minha_funcao() abaixo.
# Várias linhas de código depois...

def minha_funcao():
    a = input('Entre com a primeira palavra: ')
    b = input('Entre com a segunda palavra: ')

    print(f'A junção das duas palavras é: {a + b}')


minha_funcao()
