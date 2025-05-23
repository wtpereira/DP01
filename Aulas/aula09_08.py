def pos_neg(x):
    if x > 0:
        return 'Positivo'
    if x < 0:
        return 'Negativo'

    return 'Zero'

print(pos_neg(-10))
print(pos_neg(0))
print(pos_neg(15))

print('*' * 80)


pos_neg = lambda x: 'Positivo' if x > 0 else 'Negativo' if x < 0 else 'Zero'
print(pos_neg(-10))
print(pos_neg(0))
print(pos_neg(15))

