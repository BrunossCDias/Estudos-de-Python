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


'''print ('Exercicio 9')
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
print(f'\n\033[m 0 Número {nmr} foi divisivel {total} vezes')
if total == 2:
    print('E por isso é um número PRIMO')
else:print('Não é um número PRIMO')'''

'''#programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
#pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for c in range (1, 8):
    nascimento = int(input(f'Qual o {c}˚ ano de nascimento: '))
    idade = ano - nascimento
    if idade >= 18:
            totmaior += 1
    else:
            idade < 18
            totmenor += 1
print(f' Ao todos temos {totmaior} pessoas maiores, e {totmenor} menores de idade')'''

'''print ('Exercicio 10')
# Pograma que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float (input(f'Qual o {p}˚ peso corporal em kg : '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior} kg')
print(f'O menor peso é {menor} kg')'''

