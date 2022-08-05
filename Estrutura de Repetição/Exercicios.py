

nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
else:
     print("Todos os nomes foram listados com sucesso")


#Exercicios

print('Exercicio 1')

# Iteração com laço de repetição em uma estruta versatil com o FOR.


s = 0
for vezes in range(0, 4):
    valor = int(input('Digite um valaor: '))
    s += valor + 1
print(f'A soma de todos os valores é {s}')
print('\033[0;31;40mFIM ! \033[m')



inicio = int(input('Inicio : '))
fim = int(input('Fim : '))
passo = int(input('Passo :'))
for repetir in range (inicio, fim+1, passo ):
    print(repetir)

print('\033[0;31;40mFIM ! \033[m')

#Exercicios

print('Exercicio 2')
#Programa que faça uma contagem regressiva de 10 até 0.

from time import sleep
for regressao in range(10, -1, -1):
    sleep(1)
    print(regressao)

   
print('Exercicio 2')
# Programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0:
        soma += impares
        contador += 1
print(f'A soma de todos os {contador} numero impares multiplos de 3 é {soma}')
 #ou
s = c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        c += 1
        s += n
print(f"A soma de todos os {c} valores solicitados é {s}.")


print('Exercicio 3')
#programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

contador1 = 0
somador = 0
for repetir in range (1, 7):
    numero2 = int(input('Digite o {}˚ valor: '.format(repetir)))
    if numero2 % 2 == 0:
        somador += numero2
        contador1 += 1
print(f'Voce informou {contador1} numeros PAERES, e a soma de todos eles é {somador}')


print ('Exercicio 4')
# Programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str (input('Informe o seu SEXO : [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos ! Por Favor informe seu SEXO:  ')).strip().upper()
print(f'O seu sexo {sexo} foi registrado com sucesso. ')


print ('Exercicio 5')
from time import sleep

'''Programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
O programa deverá realizar a operação solicitada em cada caso.'''



numer1 = int(input('Digite um numero: '))
numer2 = int(input("Digite outro numero: "))
opcao = 0
while opcao != 5:
    print ('''[ 1 ] somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa ''')
    opcao = int(input("======> Escolha uma opção: "))
    if opcao == 1:
        print(f'O resutado da soma entre os dois valore é {numer1+numer2}.')
    elif opcao == 2:
        print(f'O resutado da {numer1} x {numer2} é {numer1*numer2}.')
    elif opcao == 3:
        if numer1 > numer2:
            maior = numer1
        else:
            maior = numer2
        print(f'Entre o {numer1} e o {numer2}  numero maior é {maior}.')
    elif opcao == 4:
        print('Informe os valores novamente !')
        numer1 = int(input('Digite um valor: '))
        numer2 = int(input('Digite outro valor: '))
    else:
        print('Opção invalida. Tente novamente.')
    print('=-='*10)
    print(sleep(2))
print('FIM')


print ('Exercicio 6')

from random import randint
# Programa em que o computador vai "pensar" em um número entre 0 e 10.
# O jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

computador = randint(0, 10)
print('Computador pensou em um numero entre 0 e 10, tente adivinhar..')
acertou = False
jogadas = 0
while not acertou:
    jogador = int(input('Qual seu palpite ? '))
    jogadas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais, tente novamente.')
        if jogador > computador:
            print('Menos, tente novamente.')
print(f'PARABÉNS você acertou com {jogadas} tentativas. !')
