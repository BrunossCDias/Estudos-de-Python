
# Programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for c in range(0, 5):
    valor = input('Digite um valor: ')
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Foi adicionado no fim da lista..')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posisão {pos} da lista.')
                break
            pos += 1
print(f'Os valore ordenados são eles:{lista}')

''' variavel lista recebe list'''
''' criado um FOR contador IN range de 0 até 5'''
''' criado variavel valor recebe pelo teclado um valor'''
''' definimos um IF para inserir o valor no inicio se o contador estiver na posição 0 
    OU OR se o valor for menor que o ultimo indice da lista o -1, damos um .append do valor 
    dentro lista. '''
''' Defini um ELSE'''
''' Uma variavel pos recebe 0'''
''' Enquanto WHILE pos for menor que len da lista '''
''' Se IF valor for menor ou igual ao indice da lista na posição pos, é inserido o valor na 
    mesma posiçãode pos'''
''' Feita a impressão de onde foi adicioando formatando o pos como referencia da posição do indice'''
''' Pos recebe ele mesmo mais 1 '''
''' A ultima linha imprimo os valores da lista em ordem.'''