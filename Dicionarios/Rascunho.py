



Brasil = []
Estado1 = {'UF': 'Brasilia', 'Sigla': 'DF'}
Estado2 = {'UF': 'Minas_Gerais', 'Sigla': 'MG'}
Brasil.append(Estado1)
Brasil.append(Estado2)
print(Brasil)
print((Brasil[0]['Sigla']))

'''Neste exemplo de criei uma variavel Brasil, que recebe uma lista'''
'''Criei duas variaveis Estado1, e 2 que recebe um dicionais com dois itens '''
'''Neste exemplo a lista Brasil vai receber estes itens  '''


estado = dict()
pais = list()
for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy())
print(pais)
for e in pais:
    print(e)
for e in pais:
    for v in e.values():
        print(v, end=' ')
    print(' ')
