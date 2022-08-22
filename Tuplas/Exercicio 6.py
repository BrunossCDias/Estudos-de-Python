
# Programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('amendoin', 'carro', 'pastel', 'dipirona', 'programador', 'python', 'notebook', 'frutas')
for palavras in lista:
    print(f'\nNa palavra {palavras.upper()}, tem as vogais = ', end='')
    for vogais in palavras:
        if vogais in 'aeiou':
            print(vogais.upper(), end= ' ')


''' Defini uma tupla chamada lista com diversos indices '''
''' Criei um FOR palavras para cada item IN na tupla lista '''
''' Imprimi  cada indice da tupla formatado '''
''' Defini mais um FOR para cada letras IN vogais '''
''' Defini um IF se a letras tiver IN algum "aeiou" '''
''' Dentro da identação do IF eu imprimo se a palavra haver as letras '''