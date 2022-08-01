#utilizando estruturas condicionais aninhadas simples, e compostas, aplicando os comandos if:, elif, e else:

print ('Exemplo: ')


nome = str(input('Qual seu nome? '))
if nome == 'Bruno':
    print( 'Que nome bonito !')
elif nome == 'Gustavo' or nome == 'Amanda' or nome == 'Bruna':
    print('Seu nome é bem popular no Brasil !')
elif nome in 'Paula Joao Batista Carmen':
    print('Que belo nome !'.format(nome))
else:
    print('Seu nome é bem normal !')
print('Tenho um Bom Dia, {}'.format(nome))



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
print("Para pagar uma casa de R${:.2f} em {} anos".format(casa,anos))
print('a prestacão será de R$ {:.2f}'.format(prestacao))
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
    print('{} Convertido para BINARIO é igual a {}.'.format(numero, bin(numero)[2::]))
elif opcao == 2:
    print('{} Convertido para OCTAL é {}.'.format(numero, oct(numero)[2::]))
elif opcao == 3:
    print('{} Convertido para EXADECIMAL é {}.'.format(numero, hex(numero)[2::]))


print('Exercicio 3')
'''Programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.'''

numero1 = int (input('Digite um numero :'))
numero2 = int (input('Digite outro numero :'))
if numero1 > numero2:
    print(' O numero {} é maior que o numero {}.'.format(numero1, numero2))
elif numero2 > numero1:
    print('O meior {} é maior que o numero {}.'.format(numero2, numero1))
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
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
if idade == 18:
    print('Você ja deve se alistar este ano. !')
elif idade < 18:
    faltam = 18 - idade
    print('Você tem {} anos e  ainda faltam {} anos para o seu alistamento.'.format(idade,faltam))
    anoa = ano + faltam
    print('O ano do seu alistamento será em {} !'.format(anoa))
elif idade > 18:
    faltam = idade - 18
    print('Você ja tem {} anos e deveria ter se alistado a {} anos. '.format(idade, faltam))
    anob = ano - faltam
    print('Você deveria ter se alistado em {} !'.format(anob))
    
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
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
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



print('Exercicio 6')

# Iteração com laço de repetição em uma estruta versatil com o FOR.


s = 0
for vezes in range(0, 4):
    valor = int(input('Digite um valaor: '))
    s += valor + 1
print('A soma de todos os valores é {}'.format(s))
print('\033[0;31;40mFIM ! \033[m')



inicio = int(input('Inicio : '))
fim = int(input('Fim : '))
passo = int(input('Passo :'))
for repetir in range (inicio, fim+1, passo ):
    print(repetir)

print('\033[0;31;40mFIM ! \033[m')

#Exercicios





