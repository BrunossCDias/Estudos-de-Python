import moeda


p = float(input('Digite o valor: '))
print(f'A metade de {moeda.moeda(p)}, é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)}, é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10 % deste valor, temos um total de {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo 20 % deste valor, temos um total de {moeda.moeda(moeda.diminuir(p, 20))}')
