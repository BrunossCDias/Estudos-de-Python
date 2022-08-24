
OQUE SÃO ?

lanche = ['pipoca', 'pizza','doce','biscoito']

num = [2,0,9,5,8,3,6]

As listas estarão sempre entre [], e podem ser mutaveis, para substituir ultilizamos o comando lanche[3]='refrigerante'.

Para adicionarmos no fim da lista utilizamos o metodo .append(), podemos adicionar na posição que desejar com o metodo .insert(3,'refrigerante').
Removemos itens utilizando o comando '.del lanche[3]' ou metodos '.pop(posição do indice)', ou .remove('pizza').

Podemos colocar uma lista em ordem com o metodo contem.sort(), ou em ordem recersa com metodo .sort(reverse=True) com parametro reverse=True.

num = [1, 2, 0, 4]

print(num)

num.insert(3, 5)

print(num)

num[2] = 6

num.append(9)

print(num)

num.sort()

print(num)

num.append(34)

num.append('banana')

num.insert(0, 'suco')

print(num)

num.remove('suco')

del num[3]

print(num)

num.pop()

if 'banana' in num:

    num.remove('banana')
else:

    print('Indice não encontrado')

print(num)

num.append(22)

num.append(23)

num.append(25)

num.sort()


Podemos ultilizar a estrutura de repetição FOR para cada indice em número IN enumerate(num), percorrer
um conjunto de informações e trazer o indice da variavel.

for indice, numero in enumerate(num):

    print(f'No indice {indice}  encontrei o valor {numero} !')

print('FIM DA LISTA.')

As listas podem ser compostas por outras listas, realizando uma copia dos dados com o metodo
.append[:]
    
Ex. 
numeros = list()
print(f'{numeros}')
numeros.append(num[:])
print(f'Valores é composta por {numeros}')

===============================================

OUTPUT

[1, 2, 0, 4]

[1, 2, 0, 5, 4]

[1, 2, 6, 5, 4, 9]

[1, 2, 4, 5, 6, 9]

['suco', 1, 2, 4, 5, 6, 9, 34, 'banana']

[1, 2, 4, 6, 9, 34, 'banana']

Indice não encontrado

[1, 2, 4, 6, 9, 34]

No indice 0  encontrei o valor 1 !

No indice 1  encontrei o valor 2 !

No indice 2  encontrei o valor 4 !

No indice 3  encontrei o valor 6 !

No indice 4  encontrei o valor 9 !

No indice 5  encontrei o valor 22 !

No indice 6  encontrei o valor 23 !

No indice 7  encontrei o valor 25 !

No indice 8  encontrei o valor 34 !



[]
Valores é composta por [[1, 2, 4, 6, 9, 22, 23, 25, 34]]