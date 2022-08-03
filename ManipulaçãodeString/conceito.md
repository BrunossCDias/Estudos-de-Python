   OQUE É ?

   O python considera tudo que esta entre a aspas simples ou duplas uma string.
   A Manipulação de uma sequencia de caracteres/textos ou strings 'str', é feita com as funções abaixo, é possivel também combina-las.
para que se chegue no resultado desejado no programa.
   Uma string é imutavel, a nao ser que  utilize uma função  de transformação de string e faça uma atribuição.


import split

frase = ' Cursando aulas de python '

    Fatiamento de string.
print (frase [1:5:3])


    Analise 
print(len(frase))

print (len(frase.strip()))

print(frase.count('o', 0, 13'))

print(frase.find('video'))

    Transformação, e substituição.
print(frase.replace('aulas', 'video aulas'))

print(frase)

frase.upper()

frase.lower()

frase = frase.replace('aulas', 'video aulas')

print(frase)

    Uma string será dividida em lista pelos seus espaços.
print(frase.split())

dividida = frase.split()

print(dividida)


    Imprima 2° lista, e a terceira letra da palavra splitada.
print( dividida [0][3])

' '.join(frase)

print(frase)

    O operador IN verifica se algo esta em alguma string.
    #Exemplo 
    Nome = 'Bruno Souza'
    print ('B'in Nome)