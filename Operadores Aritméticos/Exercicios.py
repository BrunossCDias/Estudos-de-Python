import math

print('Exercicio 1')

# 1º Imprima soma, multiplicação, média, divisao inteira e potenciação.
n1 = int (input ('Digite um numero : '))
n2 = int (input('Digite outro numero : '))

soma = n1 + n2
multiplicacao = n1 * n2
mdivisao = (n1 + n2) /2
divisaointeira = n1 // n2
potenciacao  = n1 ** n2
modulo = n1 % n2
print(f'A soma é {soma}, a mulplicação é {multiplicacao} a media é {mdivisao}')
print(f'A divisão inteira {divisaointeira} e a potenciacão {potenciacao}')
print (f'O resto da divisao é {modulo}')

print('Exercicio 2')
#2º Imprima antecessor, e sucessor de determinado valor digitado.

num1 = (int(input("Digite um valor ")))
num2 = num1 - 1
num3 = num1 + 1
print(f"O antecessor de {num1} é {num2}")
print(f"e o sucessor de {num1} é {num3}")


print('Exercicio 3')
#3ª Imprima o dobro, o triplo, e a raiz quadrada.

nu1 = int(input('ínsira um numero :'))
nu2 = nu1 * 2
nu3 = nu1 * 3
nu4 = nu1 ** (1/2)
print(f'O seu dobro é {nu2}, o seu triplo é {nu3}, e a raiz quadrada é {nu4}.')


print('Exercicio 4')
#4 Programa que lê dois valores, e calcule a média

portugues = float(input('Insira um valor :'))
matematica = float(input('Insira outro valor :'))
nota = (portugues + matematica)/2
print(f'A media entre as duas notas é {nota}')


print('Exercicio 5')
#5º Imprima a conversào de metros para centimetros e milimetros

metros = float (input ('Insira a medida em metros :'))
centimentros = metros * 100
milimetros = metros * 1000
print(f'{centimentros} cm.')
print(f'{milimetros} mm.')


print('Exercicio 6')
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


multiplo = int(input ('Insira um numero para saber seus multiplos : '))
for multiplicador in range(1, 11):
    print(f'{multiplo} x {multiplicador:2} = {multiplo*multiplicador}')


print('Exercicio 7')
#Imprima quantos dolares pode ser comprado com uma quantidade em reais.

real = float(input('Insira um valor ? R$ '))
dolar = real / 5.48
print(f'Com R${real:.2f} é possivel comprar  U${dolar:.2f} dolares')


print('Exercicio 8')
# Imprima a quatidade de tinta suficiente para pintar um determinada medida de parede, sabendo que 2l de tinta
#pinta uma area de 2m

largura = float(input('Qual a largura da parede ? '))
altura = float(input('Qual a altura da parede ? ' ))
area = largura * altura
print(f'Sua parede tem a dimensao de {largura} x {altura} e sua area é de {area}m.')
litros = area /2
print(f'Para pintar essa parede, vai ser necessario uma quantidade de {litros}l de tinta.')


print('Exercicio 9')
#imprima o valor do produto com 5% de desconto.

preco = float (input('Valor do produto? R$: '))
desconto = preco - (preco * 5/ 100)
print(f'O valor a ser pago com desconto de 5% é R${desconto}')


print('Exercicio 10')
#Imprima o salario de um funcionario com 15% de aumento.

salario = float (input('Salario atual R$ : '))
S_aumento = salario + (salario * 15 / 100)
print(f"Um funncionario que recebia R$ {salario}, com aumento de 15%, passará a receber R$ {S_aumento}")



print('Exercicio 11')
#Imprima a parte inteira de um numero real.

numero1 = float(input('Insira um numero : '))
print(f'O valor é {numero1} e a sua parte inteira é {math.trunc(numero1)}')

numero2 = float((input('Digite um numero : ')))
print (f' O valor digitado foi {numero2} e a sua parte inteira é {int(numero2)}')


print('Exercicio 12')


#Programa que leia o cateto oposto, o adjacente de um triangulo, e imprima o comprimemnto da hipotenusa.
# o quadrado da hipotenusa, é a soma dos quadrados dos catetos elevado a 0,5


cateoposto = float(input('Digite o valor do cateto oposto: '))
cateadjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (cateoposto ** 2 + cateadjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')

oposto = float(input('Digite o valor oposto: '))
adjacente = float(input('Digite o valor adjacente: '))
hip = math.hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hip:.2f}')
