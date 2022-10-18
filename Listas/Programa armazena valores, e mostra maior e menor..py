
# Programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
# maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()
menor = 0
maior  = 0

for valores in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {valores + 1}: ')))
    if valores == 0:
        maior = menor = numeros[valores]
    else:
        if numeros[valores] > maior:
            maior = numeros[valores]
        if numeros[valores] < menor:
            menor = numeros[valores]

print(f'Voce digitou os valores {numeros}')

print(f'O maior valor digitado foi {maior} na posição ', end='')
for v, i in enumerate(numeros):
    if i == maior:
        print(f'{v + 1}..', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for v, i in enumerate(numeros):
    if i == menor:
        print(f'{v + 1}.. ', end='')
print()