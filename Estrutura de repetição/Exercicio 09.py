#programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
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
print(f' Ao todos temos {totmaior} pessoas maiores, e {totmenor} menores de idade')