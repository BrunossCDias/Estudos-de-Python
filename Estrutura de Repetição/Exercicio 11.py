#   Programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas
# mulheres têm menos de 20 anos.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
totmulh20 = 0
nomevelho = ''
for pessoa in range (1, 5):
    print(f'******{pessoa}˚PESSOA******')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    genero = str(input('Gênero [M/F]: ')).strip()
    somaidade += idade

    if pessoa == 1 and genero in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if genero in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if genero in 'fF' and idade < 20:
        totmulh20 += 1



mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos, e se chama {nomevelho}')
print(f'O total sao {totmulh20} de mulhres com menos de 20 anos  ')
