OQUE É ?

   O python considera tudo que esta entre a aspas simples ou duplas uma string.
    A Manipulação de sequencia de caracteres/textos ou strings 'str', é feita com as funções abaixo, é possivel também combina-las.
para que se chegue no resultado desejado em seu programa.


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

    Uma string será dividida em lista pelos seus espaços.
print(frase.split())
dividida = frase.split()

    Imprima 2° lista, e a terceira letra da palavra splitada.
print( dividida [0][3])
' '.join(frase)
print(frase)

 A função IN verifica se algo esta em alguma coisa.