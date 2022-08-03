
print('Exercicio 1')
#Programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras tem ao todo (sem considerar os espaços).
# Quantas letras tem o primeiro nome.

from time import sleep
nome = str(input('Qual seu nome:')).strip()
print("Analisando seu nome....")
sleep(1)
print ('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print("Seu nome tem ao total {} letras".format(len(nome) - nome.count(" ")))
print('Seu primeiro nome tem {} letras'.format((nome.find("B"))))
print('B' in nome)


print('Exercicio 2')
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

print('Exercicio 4')

# Programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".