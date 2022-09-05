# Programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A area do terreno é de  {larg} x {comp},e o total é de {a}m²')


#Programa principal
l = (float(input('Digite a largura: ')))
c = (float(input('Digite o comprimento: ')))
area(l, c)
