i = -1
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    else:
        print(f'{i * 10}')
        print(f'outros processamentos com o {i}')

    print('Última linha do while.')
