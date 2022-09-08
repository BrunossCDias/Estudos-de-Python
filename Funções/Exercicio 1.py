# Programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A area do terreno é de  {larg} x {comp},e o total é de {a}m².')


#Programa principal
l = (float(input('Digite a largura: ')))
c = (float(input('Digite o comprimento: ')))
area(l, c)


''' Criei uma DEF chamada area, com dois parametros larg, e comp .
    Criado um programa em que duas variaveis recebem valores através do teclado 
    Chamei a função area, passando as variaves l e c 
    Declaro uma variavel a, que vai receber os parametros larg vezes comp 
    E imprimo o resutado formatado cada parametro dentro do print '''
