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
        acertou == True