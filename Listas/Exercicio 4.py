# Programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []
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
