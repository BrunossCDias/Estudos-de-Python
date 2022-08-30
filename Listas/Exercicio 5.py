
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
        print(f'A pessoa mais pesada é {pessoas[0]}')
for p in pessoas:
    if p[1] == menor:
        print(f'A pessoa mais leve é {pessoas[0]}')

