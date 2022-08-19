
# Programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,na sequência.
# No final, mostre uma listagem de preços,organizando os dados em forma tabular.


listagem = ('Lapis', 1.75,
            'Caderno', 5.00,
            'Compasso', 9.99,
            'Mochila', 15.50,
            'Estojo', 3.50,
            'Caneta', 2.50)
print("TABELA DE PREÇOS")

for tabela in range(0, len(listagem)):
    if tabela % 2 == 0:
        print(f'{listagem[tabela]:.<30}', end='')
    else:
        print(f'R${listagem[tabela]:>6.2f}')



''' Definimos um variavel tupla composta de valores em texto, e numeros'''
''' Criamos uma iteração com o FOR, e um range de 0 até o LEN da tupla  '''
''' Se IF tabela estiver em uma posição par 'resto da divisão por 2 for 0, vai listar os produtos' '''
''' Se não ELSE, vai listar os preços que estão em uma posição impar '''