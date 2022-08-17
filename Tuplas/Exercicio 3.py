
# Programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o
# menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)),
print(f'Os numeros gerados foram : {numeros}')
print(f'O maior valor é {max(numeros)}, e o menor valor é {min(numeros)} ')
