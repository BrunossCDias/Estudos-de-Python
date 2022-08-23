
# Programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
# maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for valores in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {valores}: ')))
print(f'Voce digitou os valores {numeros}')