# Programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
# partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for p in range(0, tot):
    gols.append(int(input(f'  Quantos gols foram feitos na {p + 1}˚ partida ?  ')))
jogador['Gols'] = gols.copy()
jogador['Total de Gols'] = sum(gols)
print(jogador)
