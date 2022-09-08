
OQUE É ?
    Os dicionarios são semelhantes as listas, e tuplas, porem nos DICT() podemos definir elementos com indices literais, e são identidicados 
por { }, são compostos pelos seus values e keys, usamos os metodos .items() .values() e ,keys()  

    Ex. 
        dados = {'nome':'Bruno', 'idade':25}
        print (dados['nome'])
        print (dados['idade'])

        pessoas = {'nome':'Bruna',
        'idade':22,
        'cidade':'Brasilia'
        }
   Dicionarios são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
   
    Ex 2.
        Brasil = []
    Estado1 = {'UF': 'Brasilia', 'Sigla': 'DF'}
    Estado2 = {'UF': 'Minas_Gerais', 'Sigla': 'MG'}
    Brasil.append(Estado1)
    Brasil.append(Estado2)
    print(Brasil)
    print((Brasil[0]['Sigla']))
    

'''Neste exemplo criei uma variavel Brasil, que recebe uma lista'''

'''Criei duas variaveis Estado1, e 2 que recebe um dicionário com dois itens '''

'''Neste exemplo a lista Brasil vai receber estes itens  '''

    estado = dict()
    pais = list()
    for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    pais.append(estado.copy()) 

laço para a lista.

laço para o dicionário.

    for unidade in pais:
        for e in unidade.values():
            print(f'{e}',end=' ')
            print()
    
