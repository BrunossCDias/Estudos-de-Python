# Pograma que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float (input(f'Qual o {p}˚ peso corporal em kg : '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior} kg')
print(f'O menor peso é {menor} kg')

# outra forma
peso = []
for p in range(1, 6):
    peso.append(float (input(f'Qual o {p}˚ peso corporal em kg : ')))

print (f'O maior peso é {max(peso)}')
print (f'O menor peso é {min(peso)}')

# outra forma

menor = 9999
maior = 0
for p in range(1, 6):
    peso = float(input(f'Qual o {p}˚ peso corporal em kg : '))
    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso
print(f'O maior peso é {maior} kg')
print(f'O menor peso é {menor} kg')
