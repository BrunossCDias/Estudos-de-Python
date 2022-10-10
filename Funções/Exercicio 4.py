# Programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*núm):
    """
    :param núm: Recebe os parametros desempacotados
    """
    cont = maior = 0
    print('\nAnalisando os valores inseridos')
    for n in núm:
        print(f'{n}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'\nFoi inserido {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}. ')


maior(2, 4, 8, 20)
maior(3, 5, 9, 33)
