
# Programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
valores = list()
pares = []
for c in range (0, 8):
    valores.append(int(input('Digite um valor: ')))
for par in valores:
    if par % 2 == 0:
        pares =+ par
print(pares)
print(f'Os valores são eles {valores}')