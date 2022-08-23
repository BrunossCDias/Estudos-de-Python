#Programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input("Insira um nome: ")).upper().strip()
print('A letra A aparece {}'.format(nome.count('A')))
print('A primeira letra A aparece na posição {}'.format(nome.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(nome.rfind('A')+1))

print('Exercicio 3')

# Programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um numero de 0 a 9999: '))
numero = str(numero)
print(f'analisando o numero {numero}')
print(f'Unidade: {numero[3]}')
print(f'Dezena : {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar:{numero[0]}')


