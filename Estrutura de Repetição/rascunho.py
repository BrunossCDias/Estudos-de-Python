'''soma = contador = 0
for c in range(1, 8):
    numero = int(input(f'Digite o {c} aqui: '))
    if numero % 2 == 0:
            soma += numero
            contador += 1
print(f'O total de numeros pares foi  {contador}, e soma entre eles é {soma}')'''

'''numr = 1
imprs = 0
contad = 0
while numr != 0:
    numr = int(input('Digite um vlr: '))
    if numr != 0:
        if numr % 3 == 0:
            imprs +=numr
            contad += 1
print(f'a soma de todos os numeros {contad} impares é {imprs}')'''


print ('Exercicio 8')
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