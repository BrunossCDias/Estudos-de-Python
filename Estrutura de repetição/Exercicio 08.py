# Programa que leia um número inteiro e diga se ele é ou não um número primo.
total = 0
nmr = int(input('Digite um valor: '))
for contad in range(1, nmr + 1):
    if nmr % contad == 0:
        print('\033[m', end=' ')
        total+= 1
    else:
        print('\033[31m', end=' ')
    print(f'{contad}', end=' ')
print(f'\n\033[m0 Número {nmr} foi divisivel {total} vezes')
if total == 2:
    print('E por isso é um número PRIMO')
else:print('Não é um número PRIMO')