


pessoas = {'Nome': 'Bruno', 'Sexo': 'M', 'Idade': 22 }
print(pessoas)
del pessoas['Nome']
pessoas['Nome'] ='Landro'
pessoas['Peso'] = 45
for k, v in pessoas.items():
    print(f'{k} = {v}')

lista = list()
lista.append(pessoas)
print(pessoas['Nome'])
print(lista)
