
# Oque é ? 

Estruturas de controle condicional aninhadas simples, e compostas, são algoritmos bem estrurados por comandos  if:, elif, e else:

#Para que serve?

Para definirmos prioridade a cada condição.


Exemplo:


nome = str(input('Qual seu nome? '))
if nome == 'Bruno':
    print( 'Que nome bonito !')
elif nome == 'Gustavo' or nome == 'Amanda' or nome == 'Bruna':
    print('Seu nome é bem popular no Brasil !')
elif nome in 'Paula Joao Batista Carmen':
    print('Que belo nome !'.format(nome))
else:
    print('Seu nome é bem normal !')
print('Tenho um Bom Dia, {}'.format(nome))
