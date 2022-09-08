# Programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento : '))
dados['Idade'] = datetime.now().year - ano
dados['CTPS'] = int(input('CTPS (0 não possui): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Remuneração R$:  '))
    dados['Aposentadorioa'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-=' * 20)
for k, v in dados.items():
    print(f'  -{k} tem o valor {v}')
