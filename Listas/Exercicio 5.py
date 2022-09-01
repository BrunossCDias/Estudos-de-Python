
# Programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digita o peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = (str(input('Quer continyuar o cadastro ? [S/N]')))
    if continuar in 'Nn':
        break

print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior} Kg')
print(f'O menor peso foi de {menor} Kg')

for p in pessoas:
    if p[1] == maior:
        print(f'A pessoa mais pesada é {p[0]}')
for p in pessoas:
    if p[1] == menor:
        print(f'A pessoa mais leve é {p[0]}')

''' Defino as variaveis dados, pessoas como umq lista'''
''' Defino os valores para maior em menor como zero'''
''' Crio uma estrutura de repetição com enquanto While for True'''
''' Insiro um append para variavel dados receber os dados através do teclado com um input '''
''' Defino uma condição IF se o len da variavel pessoa for 0, defino as variaveis maior e menor receber os valores da lista na posição 0'''
''' Defino um ELSE dentro da identação defino um IF para verificar se o dado do peso é maior que a varivel, se for maior, ela recebe este valor maior'''
''' O mesmo faço para o menor valor'''
''' Defino um condição IF para a variavel continuar em [S/N], para quebrar ou nao o laço '''
''' Imprimo os valores maior, menor, e o len da lista pessoa '''
''' Defino uma estrura de repetição FOR para cada P na lista de pessoas, crio uma condição IF para o valor  do indice[1] da lista pessoas se ele for igual
 a variavel maior, imprimo o indice [0] da variavel P.'''
''' E faço o mesmo para encontrar a pessoa  mais leve.'''