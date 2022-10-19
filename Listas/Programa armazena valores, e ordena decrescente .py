# Programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar : [S/N]'))
    if continuar in 'Nn':
        break
print(f'Foi digitado {len(valores)} valores')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente é {valores}')
if 5 in valores:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')

''' Variavel valores recebe uma lista '''
''' Equanto a condição for True, a variavel valores rececebe um valor inteiro através do teclado'''
''' Crio uma variavel continuar que recebe uma resposta através do teclado'''
''' Se variavel continuar receber um Nn o loop é parado com um break'''
''' Imprimo a quantidade de valores digitado formatado com o len de valores'''
''' Crio um metodo de .sort com reverse True da variavel valores '''
''' Imprimo os valores em ordem decrescente'''
''' Crio uma condião para o valor 5 se estiver ou não na variavel valores'''
