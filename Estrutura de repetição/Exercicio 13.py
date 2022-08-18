#Programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
#digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e a soma entre eles (desconsiderando o flag).

numero = soma = contador = 0
while numero != 999:
    numero = int(input('Digite um valor par fazer a soma ou, [ 999 para parar]: '))
    if numero != 999:
        soma += numero
        contador += 1

print(f'A soma entre todos os {contador} valores é {soma}')
