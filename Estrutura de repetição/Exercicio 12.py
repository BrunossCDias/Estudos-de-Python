# Programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
numero = int(input('Quantos termos deseja mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} ---{t2}', end= '')
contador = 3
while contador <= numero:
    t3 = t1 + t2
    print(f'---{t3}', end='')
    contador += 1
    t1 = t2
    t2 = t3
print('---FIM')