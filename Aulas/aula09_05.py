# booleanos
verdadeiro = True
falso = False

if verdadeiro:
    print('Verdadeiro')
else:
    print('Falso')

if falso:
    print('Verdadeiro')
else:
    print('Falso')

print('*' * 80)

if 1:
    print('Verdadeiro')
else:
    print('Falso')

if -1000:
    print('Verdadeiro')
else:
    print('Falso')

if 0:
    print('Verdadeiro')
else:
    print('Falso')

print('*' * 80)

if 1.0:
    print('Verdadeiro')
else:
    print('Falso')

if 0.0:
    print('Verdadeiro')
else:
    print('Falso')

if -3.14:
    print('Verdadeiro')
else:
    print('Falso')


print('*' * 80)

if '1':
    print('Verdadeiro')
else:
    print('Falso')

if '0':
    print('Verdadeiro')
else:
    print('Falso')

if '':
    print('Verdadeiro')
else:
    print('Falso')


print('*' * 80)

falsy = [None, False, 0, 0.0, '', [], {}, tuple(), set()]
truthy = [True, 1, 3.14, 'alura', [1, 2, 3], {'chave': 'valor'}, (1, 2, 3), {1, 2, 3}]


for elemento in falsy:
    if elemento:
        print(f'{elemento} é Verdadeiro')
    else:
        print(f'{elemento} é Falso')

print('*' * 80)

for elemento in truthy:
    if elemento:
        print(f'{elemento} é Verdadeiro')
    else:
        print(f'{elemento} é Falso')

print('*' * 80)


class Aluno:
    pass

aluno = None

if aluno:
    print('Verdadeiro')
else:
    print('Falso')


print('*' * 80)

aluno = Aluno()

if aluno:
    print('Verdadeiro')
else:
    print('Falso')


print('*' * 80)
