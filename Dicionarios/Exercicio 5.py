# Programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cadastro = list()
pessoa = dict()
soma = media = 0
pessoa.clear()
while True:
    while True:
        pessoa['nome'] = str(input('Digite o nome: '))
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO ! Por favor, apenas M ou F')
    pessoa['idade'] = int(input('Digite a idade : '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar ? [S/N]')).upper()[0]
        if continuar in 'SN':
            break
            print('ERRO ! Por favor, apenas S ou N.')
    if continuar == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(cadastro)} pessoas cadastradas.')
media = soma / len(cadastro)
print(f'A média de todas as idades é de {media:5.2f} anos')
print(f' As mulheres cadastradas foram ', end='')
for mulher in cadastro:
    if mulher['sexo'] == 'F':
        print(f'{mulher["nome"]}', end=', ')
print()
print('Pessoas que estão acima da média : ')
for p in cadastro:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}, ', end='')
