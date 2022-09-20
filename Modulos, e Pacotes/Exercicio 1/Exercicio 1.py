# Programa que importa módulo e use algumas funções conforme a chamada do programa.

from uteis import moeda

p = float(input('Digite o valor: '))
print(f'A metade de {p}$ é {moeda.metade(p)}$')
print(f'O dobro de {p}$, é {moeda.dobro(p)}$')
print(f'Mais 10 % deste valor, temos um total de {moeda.aumentar(p, 10)}$')
print(f'Menos 20 % deste valor, temos um total de {moeda.diminuir(p, 20)}$')
