import Moeda


p = float(input('Digite o valor: '))
print(f'A metade de {Moeda.moeda(p)}, é {Moeda.moeda(Moeda.metade(p))}')
print(f'O dobro de {Moeda.moeda(p)}, é {Moeda.moeda(Moeda.dobro(p))}')
print(f'Aumentando 10 % deste valor, temos um total de {Moeda.moeda(Moeda.aumentar(p, 10))}')
print(f'Diminuindo 20 % deste valor, temos um total de {Moeda.moeda(Moeda.diminuir(p, 20))}')
