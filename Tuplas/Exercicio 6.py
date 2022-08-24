
# Programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla_de_palavras = ('aaeeiioouu','amendoin', 'carro', 'pastel', 'dipirona', 'programador', 'python', 'notebook', 'frutas',)
for palavra in tupla_de_palavras:
    print(f'\nNa palavra {palavra.upper()}, tem as vogais = ', end='')
    vogais_encontradas = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            if letra.upper() not in vogais_encontradas:
                vogais_encontradas.append(letra.upper())
    print(sorted(vogais_encontradas),end= ' ')


''' Defini uma tupla chamada lista com diversos indices '''
''' Criei um FOR palavras para cada item IN na tupla lista '''
''' Imprimi  cada indice da tupla formatado '''
''' Defini mais um FOR para cada letras IN vogais '''
''' Defini um IF se a letras tiver IN algum "aeiou" '''
''' Dentro da identação do IF eu imprimo se a palavra haver as letras '''
