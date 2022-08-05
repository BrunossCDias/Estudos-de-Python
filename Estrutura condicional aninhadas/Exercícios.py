

# Exemplo .

nome = str(input('Qual seu nome? '))
if nome == 'Bruno':
    print('Que nome bonito !')
elif nome == 'Gustavo' or nome == 'Amanda' or nome == 'Bruna':
    print('Seu nome é bem popular no Brasil !')
elif nome in 'Paula Joao Batista Carmen':
    print(f'Que belo nome {nome} !')
else:
    print('Seu nome é bem normal !')
print(f'Tenho um Bom Dia, {nome}')


#Exercicios

print('Exercicio 1')
'''Programa que avalie um emprestimo bancario para a compra de uma casa
O programa vai perguntar o valor da casa, o salario do comprador e em quantos 
anos ele vai pagar a divida.
Calcule o valor da prestação mensal, sabendo-se que ele nao pode exceder 30% do salario
ou então o emprestimo sera negado.'''

casa = float(input('Qual o valor a ser financiado ? '))
salario = float(input('Qual salario mensal ?'))
anos = int (input('Em quantos anos vai pagar ?'))
prestacao =  casa / (anos * 12)
minimo = salario * 30 / 100
print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos")
print(f'a prestacão será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('Você pode realizar o financiamento.')
else:
    print('Você não pode realizar o financiamento.')



print('Exercicio 2')
'''Programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a 
base de conversão.'''
numero = int(input('Qual numero inteiro ?' ))
print('''Escolha uma das opções abaixo para conversão :
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para EXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{numero} Convertido para BINARIO é igual a {bin(numero)[2::]}.')
elif opcao == 2:
    print(f'{numero} Convertido para OCTAL é {oct(numero)[2::]}')
elif opcao == 3:
    print(f'{numero} Convertido para EXADECIMAL é {hex(numero)[2::]}')


print('Exercicio 3')
'''Programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.'''

numero1 = int (input('Digite um numero :'))
numero2 = int (input('Digite outro numero :'))
if numero1 > numero2:
    print(f' O numero {numero1} é maior que o numero {numero2}.')
elif numero2 > numero1:
    print('O meior {numero2} é maior que o numero {numero1}.')
else:
    print('Não existe valor maior, os dois são iguais.')

print('Exercicio 4')
'''Programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do 
tempo do alistamento. Programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = date.today().year
nascimento = int(input('Qual ano de nascimento ? '))
idade = ano - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}.')
if idade == 18:
    print('Você ja deve se alistar este ano. !')
elif idade < 18:
    faltam = 18 - idade
    print(f'Você tem {idade} anos e  ainda faltam {faltam} anos para o seu alistamento.')
    anoa = ano + faltam
    print(f'O ano do seu alistamento será em {anoa} !')
elif idade > 18:
    faltam = idade - 18
    print(f'Você ja tem {idade} anos e deveria ter se alistado a {faltam} anos. ')
    anob = ano - faltam
    print(f'Você deveria ter se alistado em {anob} !')
    
print('Exercicio 5')
#Crie um programa que jogue com o usuario, PREDRA,PAPEL e TESOURA.

from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2 )
print('''Escolha uma das opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')

print("-=" * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('Jogo ficou \033[0;31;40mEMPATADO !\033[m')
    elif jogador == 1:
        print('O computador \033[0;31;40mPERDEU !\033[m')
    elif jogador == 2:
        print('O Computador \033[0;31;40mVENCEU !\033[m')
    else:
        print('Jogada \033[0;31;40mINVALIDA !\033[m')

if computador == 1:
    if jogador == 1:
        print('O Jogo ficou \033[0;31;40mEMPATADO !\033[m')
    elif jogador == 0:
        print('O Computador \033[0;31;40mPERDEU !\033[m')
    elif jogador == 2:
        print('O Computador \033[0;31;40mPERDEU !\033[m')
    else:
        print('Jogada \033[0;31;40mINVALIDA !\033[m')

if computador == 2:
    if jogador == 2:
        print('O Jogo ficou \033[0;31;40mEMPATADO !\033[m')
    elif jogador == 1:
        print('O Computador \033[0;31.40mVENCEU !\033[m')
    elif jogador == 0:
        print('O Computador \033[0;;31;40mPERDEU !\033[m')
