# 1º Imprima soma, multiplicação, média, divisao inteira e potenciação.
n1 = int (input ('Digite um numero : '))
n2 = int (input('Digite outro numero : '))

soma = n1 + n2
multiplicacao = n1 * n2
mdivisao = (n1 + n2) /2
divisaointeira = n1 // n2
potenciacao  = n1 ** n2
modulo = n1 % n2
print(f'A soma é {soma}, a mulplicação é {multiplicacao} a media é {mdivisao}')
print(f'A divisão inteira {divisaointeira} e a potenciacão {potenciacao}')
print (f'O resto da divisao é {modulo}')