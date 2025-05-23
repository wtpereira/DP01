def media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4


resultado = media(3.4, 5.6, 9, 1.2)
print(f'A média das notas é {resultado}')

print("*" * 80)

media_lambda = lambda n1, n2, n3, n4: (n1 + n2 + n3 + n4) / 4

resp = media_lambda(3.4, 5.6, 9, 1.2)
print(f'A média das notas é {resp}')
