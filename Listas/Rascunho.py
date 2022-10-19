
valores = list()
valores.append(5)
valores.append(6)
valores.append(4)

for cont in range(0,3):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c+1}, encontrie o valor {v}')
print('Cheguei ao final da lista')
print(sorted(valores))