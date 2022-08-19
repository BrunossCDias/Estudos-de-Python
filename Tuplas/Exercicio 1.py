

#Programa que tenha uma tupla totalmente preenchida comuma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
while True:
    while True:
        valor = int(input('Digite um valor entre 0 e 20: '))
        if 0 <= valor <= 20:
            break
        print('Tente novamente...', end='')
    print(f'Você digitou o numero {contagem[valor]}')
    continuar = str(input('Tentar novamente ? [S/N]: ')).upper().strip()
    if continuar == 'N':
        break
print('-='*20)
print('PROGRAMA ENCERRADO')



