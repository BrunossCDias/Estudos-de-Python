# Programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar.
# No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.


total18 = homens = mulheres = 0
while True:
    idade = int(input('Qual a idade: '))
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Digite o genero: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if genero == 'M':
        homens += 1
    if genero == 'F':
        if idade < 20:
            mulheres += 1


    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O total de pessoas maiores de 18 anos é {total18}')
print(f'O total de homens cadastrados foram {homens}')
print(f'O total de mulheres com menos de 20 anos é {mulheres}')
