# Tendo um CPF dentro de uma string no formato '12345678900',
# desenvolva um programa para imprimir esse CPF no formato: '123.456.789-00'

cpf = '12345678965'

# 1ª solução:

s1 = ''
for i in range(0, 3, 1):
    s1 += cpf[i]

s2 = ''
for i in range(3, 6, 1):
    s2 += cpf[i]

s3 = ''
for i in range(6, 9, 1):
    s3 += cpf[i]

s4 = ''
for i in range(9, 11, 1):
    s4 += cpf[i]

print(f'{s1}.{s2}.{s3}-{s4}')

# 2ª solução:

s5 = cpf[0:3:1]
s6 = cpf[3:6:1]
s7 = cpf[6:9:1]
s8 = cpf[9:11:1]

print(f'{s5}.{s6}.{s7}-{s8}')

# 3ª solução: caso eu não queira criar variáveis temporárias:
print(f'{cpf[0:3:1]}.{cpf[3:6:1]}.{cpf[6:9:1]}-{cpf[9:11:1]}')

