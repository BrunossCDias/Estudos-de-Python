# Programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
totalcedula = 0
cedula = 50
saldo = float(1500.00)
deposito = saque= opcao = 0
print('='*30)
print( 'BEM VINDO AO BANCO BRASILEIRO')
print('='*30)
while opcao != 4:
    print('''[ 1 ] Saldo
[ 2 ] Deposito
[ 3 ] Saque
[ 4 ] Sair  ''')
    opcao = int(input('======> Escolha a opção que deseja: '))
    if opcao == 1:
        print(f'O seu saldo em conta é de  R${saldo:.2f}')
    elif opcao == 2:
        soma = float(input('Qual valor R$ do seu deposito: '))
        saldo += soma
        print( f'Você depositou R${soma}, e seu saldo é de {saldo:.2f}')

    elif opcao == 3:
        saque = float(input('Qual valor deseja sacar ? '))
        totalsaque = saque
        print( f'Você sacou R${saque:.2f}')
        saldo -= saque
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
        break

print('PRONTO, retire o dinheiro.')
while True:
    if totalsaque >= cedula:
        totalsaque -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'{totalcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if totalsaque == 0:
            break

print('Volte sempre !')
