
# Programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
print('-='*20)
numero = (int(input('Digite um valor: ')),
          int(input('Digite outro valor: ')),
          int(input('Digite mais um valor: ')),
          int(input('Digite o ultimo valor: ')))
print(f'Os valores digitados foram {numero}')
print(f'O valor 9 aparece {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O valor 3 aparece na {numero.index(3)+1}˚ posição.')
else:
    print('Não existe valor 3 em nenhuma posição')
print('Os valores pares são eles ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=', ')
print('FIM DO PROGRAMA')

'''Criamos a variavel número lendo INPUT 4 valores pelo teclado, 
aberto no inicio e fechado parentezes noo ultimo indice da tupla '''
'''Utilizamos a função build COUNT para contar quantas vezes aparecem o valor 9 '''
'''Definimos um IF se o numero 3 aparece na tupla, e mostramos a indexação 
do valor 3 somando o index com mais 1, pois as posiçoes sempre começão em 0'''
'''Definimos um FOR para cada n IN numero'''
'''Será impresso na tela os valores pares, se IF cada n o resto da divisao por 2 for igual a 0.  '''
