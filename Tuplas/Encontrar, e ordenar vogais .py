
# Programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

#Coloca o ‘aeiou’ em uma variável.
#Utiliza ela no if letra in vogais

#E na parte de baixo faz um for vogal  in vogais
#If vogal in vogais_encontradas:
   #Print vogal

vogais = 'aeiou'
tupla_de_palavras = ('UIEAOXaeiox', 'amendoin', 'carro', 'pastel',
                     'dipirona', 'programador', 'python',
                     'notebook', 'frutas',)
for palavra in tupla_de_palavras:
    print(f'\nNa palavra {palavra}, tem as vogais = ', end='')
    vogais_encontradas = []
    for letra in palavra.lower():
        if letra in vogais and letra not in vogais_encontradas:
            vogais_encontradas.append(letra)

    for vogal in vogais:
        if vogal in vogais_encontradas:
            print(vogal, end=' ')



''' Defini uma tupla chamada tupla_de_palavras.'''
''' Criei um loop FOR palavra para cada item IN tupla_de_palavras. '''
''' Imprimi  cada indice da tupla formatado. '''
''' Variavel vogais_encontradas recebe uma lista. '''
''' Criei loop FOR para cada letra na variavel palavra convertida para minuscula  '''
''' Defini um IF identado no loop se a letras estiver IN "aeiou" '''
''' Dentro da identação do IF criei mais um IF se a letra nao estiver na variavel vogal_encontradas,
 a variavel recebe com o metodo .append a letra. '''
''' Na ultima linha fora do loop eu imprimi a variavel com todas as vogais sem repetição'''