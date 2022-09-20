# Programa que importa módulo e use algumas funções conforme a chamada do programa.

from moeda import metade, dobro, aumentar, diminuir

p = float(input('Digite o valor: '))
print(f'A metade de {p}$ é {metade(p)}$')
print(f'O dobro de {p}$, é {dobro(p)}$')
print(f'Mais 10 % deste valor, temos um total de {aumentar(p, 10)}$')
print(f'Menos 20 % deste valor, temos um total de {diminuir(p, 20)}$')
