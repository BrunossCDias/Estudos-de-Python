
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
