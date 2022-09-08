
# Programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dados = dict()
dados['Nome'] = str(input('Digite o nome do aluno: '))
dados['Nota'] = float(input(f'Digite a nota de {dados["Nome"]}: '))
if dados['Nota'] >= 7:
        dados['Situação'] = 'Aprovado'
elif 5 <= dados['Nota'] < 7:
        dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'
for nota, status in dados.items():
    print(f'{nota}, é igual a {status}  ')


''' Criado uma variavel dados como um dicionario.'''
''' A variavel dadaos recebe o nome e a nota através do teclado com um input'''
''' Definido um condição IF para nota se for maior ou igual a 7, é adicionado uma key, e value como aprovado no dicionario'''
''' Da mesma forma é feita com as condições ELIF, e ELSE '''
''' Criada um estrutura de repetição, para imprimir cada .items do dicionario'''
