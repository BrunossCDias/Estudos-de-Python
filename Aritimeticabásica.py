# Operadores aritméticos

a = 2
b = 3
c = 5

print ( a + b )
print ( a + b - c )
print ( b / a )
print ( b // a )
print ( c % a )
print ( a ** a )

import math
import random


print('Ex 1')
# 1º Imprima soma, multiplicação, média, divisao inteira e potenciação.
n1 = int (input ('Digite um numero : '))
n2 = int (input('Digite outro numero : '))

s = n1 + n2
m = n1 * n2
d = (n1 + n2) /2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, a mulplicação é {m} a media é {d}')
print(f'A divisão inteira {di} e a potenciacão {e}')


print('Ex 2')
#2º Imprima antecessor, e sucessor
num1 = (int(input("Digite um valor ")))
num2 = num1 - 1
num3 = num1 + 1
print(f"O antecessor de {num1} é {num2} ")
print(f"e o sucessor de {num1} é {num3}")


print('Ex 3')
#3ª imprima o dobro, triplo, e a raiz quadrada
nu1 = int(input('ínsira um numero :'))
nu2 = nu1 * 2
nu3 = nu1 * 3
nu4 = nu1 ** (1/2)
print(f'O seu dobro é {nu2}, o seu triplo é {nu3}, e a raiz quadrada é {nu4}.')


print('Ex 4')
#4 programa que lê dois valores, e calcule a média

portugues = float(input('Insira um valor :'))
matematica = float(input('Insira outro valor :'))
nota = (portugues + matematica)/2
print(f'A media entre das notas sao {nota}')


print('Ex 5')
#5º Imprima a conversào de metros para centimetros e milimetros

metros = float (input ('Insira a medida em metros :'))
centimentros = metros * 100
milimetros = metros * 1000
print(f'{centimentros} cm.')
print(f'{milimetros} mm.')


print('Ex 6')
# Imprima os multiplos de um determinado valor.
mult = int (input ('Insira um numero para saber seus multiplos : '))
print('{} x {:2} = {}'.format(mult, 1, mult*1))
print('{} x {:2} = {}'.format(mult, 2, mult*2))
print('{} x {:2} = {}'.format(mult, 3, mult*3))
print('{} x {:2} = {}'.format(mult, 4, mult*4))
print('{} x {:2} = {}'.format(mult, 5, mult*5))
print('{} x {:2} = {}'.format(mult, 6, mult*6))
print('{} x {:2} = {}'.format(mult, 7, mult*7))
print('{} x {:2} = {}'.format(mult, 8, mult*8))
print('{} x {:2} = {}'.format(mult, 9, mult*9))
print('{} x {:2} = {}'.format(mult, 10, mult*10))


print('Ex 7')
#Imprima quantos dolares pode ser comprado com uma quantidade em reais.

real = float(input('Insira um valor ? R$ '))
dolar = real / 5.48
print('Com R${:.2f} é possivel comprar  U${:.2f} em dolares'.format(real, dolar))


print('Éx 8')
# Imprima a quatidade de tinta suficiente para pintar um determinada medida de parede, sabendo que 2l de tinta
#pinta uma area de 2m

largura = float(input('Qual a largura da parede ? '))
altura = float(input('Qual a altura da parede ? ' ))
area = largura * altura
print('Sua parede tem a dimensao de {} x {} e sua area é de {}m.' .format(largura, altura,area))
litros = area /2
print(f'Para pintar essa parede, vai ser necessario a quantidade de {litros}l de tinta.')


print('Éx 9')
#imprima o valor do produto com 5% de desconto.

preco = float (input('Valor do produto? R$: '))
desconto = preco - (preco * 5/ 100)
print(f'O valor a ser pago com desconto de 5% é R${desconto}')


print('Éx 10')
#Imprima o salario de um funcionario com 15% de aumento.

salario = float (input('Salario atual R$ : '))
S_aumento = salario + (salario * 15 / 100)
print(f"Um funncionario que recebia R$ {salario}, com aumento de 15%, passará a receber R$ {S_aumento}")



print('Éx 11')
#Imprima a parte inteira de um numero real.

numero = float(input('Insira um numero : '))
print('O valor é {} e a sua parte inteira é {}'.format(numero,math.trunc(numero)))

num = float((input('Digite um numero : ')))
print (' O valor digitado foi {} é a sua parte inteira é {}'.format(num, int(num)))


print('Éx 12')

#Programa que leia o cateto oposto, o adjacente de um triangulo, e imprima o comprimemnto da hipotenusa.
# o quadrado da hipotenusa, é a soma dos quadrados dos catetos elevado a 0,5

catoposto = float(input('Digite o valor do cateto oposto: '))
catadjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (catoposto ** 2 + catadjacente ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

oposto = float(input('Digite o valor oposto: '))
adjacente = float(input('Digite o valor adjacente: '))
hip = math.hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hip))
