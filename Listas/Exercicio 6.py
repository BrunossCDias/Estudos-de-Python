# Programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados
# os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
valores = list()
pares = list()
impares = list()
for c in range(0, 8):
    valores.append(int(input('Digite um valor: ')))
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'Os valores digitados são eles {valores}')
print(f'Os valores pares inseridos são:  {pares}')
print(f'Os valores impares inseridos são: {impares}')