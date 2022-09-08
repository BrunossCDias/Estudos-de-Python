#Programa que leia o cateto oposto, o adjacente de um triangulo, e imprima o comprimemnto da hipotenusa.
# o quadrado da hipotenusa, é a soma dos quadrados dos catetos elevado a 0,5
import math

cateoposto = float(input('Digite o valor do cateto oposto: '))
cateadjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (cateoposto ** 2 + cateadjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')

oposto = float(input('Digite o valor oposto: '))
adjacente = float(input('Digite o valor adjacente: '))
hip = math.hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hip:.2f}')