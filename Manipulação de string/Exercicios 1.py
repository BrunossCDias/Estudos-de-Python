

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
print('Seu primeiro nome tem {} letras'.format((nome.find('b'))))
print('B' in nome)
