# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

brasileirao = ('Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Internacional',
               'Atlético-MG', 'América-MG', 'Bragantino', 'Santos', 'SãoPaulo', 'Botafogo', 'Goiás',
               'Ceará', 'Fortaleza', 'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print('-='*30)
print(f'Os 5 primeiros times da tabela do brasileirão são eles {brasileirao[0:5]}')
print('-='*30)
print(f'Os 4 ultimos times da tabela do brasileirão são eles {brasileirao[-4:]}')
print('-='*30)
print(f'Em ordem alfabetica {sorted(brasileirao)}')
print('-='*30)
print(f'O time São Paulo esta na posição {brasileirao.index("SãoPaulo")+1}˚ posição da tabela')
