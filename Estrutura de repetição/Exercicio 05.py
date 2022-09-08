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
    print ('''  [ 1 ] somar
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
