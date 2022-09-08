from random import randint
# Programa em que o computador vai "pensar" em um número entre 0 e 10.
# O jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

computador = randint(0, 10)
print('Computador pensou em um número entre 0 e 10, tente adivinhar..')
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
