def formata_data(dia, mes, ano):
    return f'{dia:02d}/{mes:02d}/{ano}'


print(formata_data(15, 5, 2025))

print(formata_data(1, 1, 2025))


print(formata_data(5, 26, 2025))  # vai imprimir uma formatação errada.

print(formata_data(2025, 5, 26)) # vai imprimir uma formatação errada.


print(formata_data(mes=5, dia=26, ano=2025)) # vai corrigir a formatação da linha 10.

print(formata_data(ano=2025, mes=5, dia=26)) # vai corrigir a formatação da linha 12.

print(formata_data(mes=1, ano=2025, dia=30))

