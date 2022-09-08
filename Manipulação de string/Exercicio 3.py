# Programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um numero de 0 a 9999: '))
numero = str(numero)
print(f'analisando o numero {numero}')
print(f'Unidade: {numero[3]}')
print(f'Dezena : {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar:{numero[0]}')
