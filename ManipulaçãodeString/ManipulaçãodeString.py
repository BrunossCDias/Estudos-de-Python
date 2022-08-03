# Manipulando cadeias de caracteres/textos ou strings com as operações abaixo, e é possivel combina-las.


import split

frase = ' cursando aulas de python '

print (frase [1:5:3])
print(frase.upper())
print(frase.count('o'))
print(len(frase))
print (len(frase.strip()))
print(frase.replace('aulas', 'video aulas'))
print(frase)
frase = frase.replace('aulas', 'video aulas')
print(frase)
print(frase.find('video'))

# uma string será dividida em lista pelos seus espaços
print(frase.split())
dividida = frase.split()
# imprima 2° lista e a terceira letra da palavra splitada.
print( dividida [0][3])
' '.join(frase)
print(frase)

print('Exercicio 1')
#Programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras tem ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

from time import sleep
nome = str(input('Qual seu nome:')).strip()
print("Analisando seu nome....")
sleep(2)
print ('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print("Seu nome tem ao total {} letras".format(len(nome) - nome.count(" ")))
print('Seu primeiro nome tem {} letras'.format((nome.find(" "))))

print('Exercicio 2')
#Programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = str(input("Insira um nome: ")).upper().strip()
print('A letra A aparece {}'.format(nome.count('A')))
print('A primeira letra A aparece na posição {}'.format(nome.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(nome.rfind('A')+1))



