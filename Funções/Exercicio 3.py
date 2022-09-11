# Programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*15)
    print(f'Contagem de {i} até {f} de {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p


contador(1, 5, 1)
contador(50, 10, 10)
print()
print('Agora é a sua vez !! ')
init = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(init, fim, passo)
