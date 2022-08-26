
# Programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá
# dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = list()
while True:
    valores = input('Digite um valor: ')
    if valores not in numeros:
        numeros.append(valores)
        print('Valor adicionado....')
    else:
        print('Valor repetido, tente novamente....')
    resposta = str(input('Deseja continuar: [S/N]'))
    if resposta in 'Nn':
        break
print(f'Os numeros digitados foram:{sorted(numeros)}')
