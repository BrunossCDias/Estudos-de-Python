
# Programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('amendoin', 'carro', 'pastel', 'dipirona', 'programador', 'python', 'notebook', 'frutas')
for palavra in lista:
    print(f'\nNa palavra {palavra.upper()}, tem as vogais = ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra.upper(), end= ' ')


''' Defini uma tupla chamada lista com diversos indices '''
''' Criei um FOR palavras para cada item IN na tupla lista '''
''' Imprimi  cada indice da tupla formatado '''
''' Defini mais um FOR para cada letras IN vogais '''
''' Defini um IF se a letras tiver IN algum "aeiou" '''
''' Dentro da identação do IF eu imprimo se a palavra haver as letras '''





vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'TRABALHAR')

for palavra in palavras:
    print(f'Na palavra {palavra} temos as vogais: ', end='')

    for letras in palavra:
        if (letras.lower() in vogais):
            print(f'{letras.lower()}', end=' ')
    print()