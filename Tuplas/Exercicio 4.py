
# Programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numero = (int(input('Digite um valor: ')),
          int(input('Digite outro valor: ')),
          int(input('Digite mais um valor: ')),
          int(input('Digite o ultimo valor: ')))
print(f'Os valores digitados foram {numero}')
print(f'O valor 9 aparece {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O valor 3 aparece na {numero.index(3)+1}˚ posição.')
else:
    print('Não existe valor 3 em nenhuma posição')
print('Os valores pares são eles ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')