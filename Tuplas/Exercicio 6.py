
# Programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla_de_palavras = ('aaeeiioouu','amendoin', 'carro', 'pastel',
                     'dipirona', 'programador', 'python', 'notebook',
                     'frutas',)
for palavra in tupla_de_palavras:
    print(f'\nNa palavra {palavra.upper()}, tem as vogais = ', end='')
    vogais_encontradas = []
    for letra in palavra:
        if letra.lower() in 'aeiou':
            if letra.upper() not in vogais_encontradas:
                vogais_encontradas.append(letra.upper())
    print(sorted(vogais_encontradas),end= ' ')


''' Defini uma tupla chamada tupla_de_palavras com diversos indices '''
''' Criei um loop FOR palavra para cada item IN tupla_de_palavras. '''
''' Imprimi  cada indice da tupla formatado. '''
''' A variavel vogais_encontradas recebe uma lista'''
''' Criei loop FOR para cada letra na vaiavel palavra  '''
''' Defini um IF identado no loop se a letras minuscula estiver IN "aeiou" '''
''' Dentro da identação do IF criei mais um IF se a letra nao estiver na variavel vogal_encontradas, a variavel recebe com um metodo .append a letra em maiusculo. '''
''' Na ultima linha fora do loop eu imprimi a variavel com todas as vogais sem repetição'''