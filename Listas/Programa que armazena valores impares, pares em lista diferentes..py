#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = list()
impares = list()
pares = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar ? [S/N] '))
    if resposta in 'nN':
        break

for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista completa é formada pelos valores {lista}')
print(f'A lista de valores pares são {pares} ')
print(f'A lista de valores impares são {impares}')