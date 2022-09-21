# Modifiquei as funções que foram criadas nos programas anteriores para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda().

import Calculos


p = float(input('Digite o valor: '))
print(f'A metade de {Calculos.moeda(p)}, é {Calculos.metade(p, True)}')
print(f'O dobro de {Calculos.moeda(p)}, é {Calculos.dobro(p, True)}')
print(f'Aumentando 10 % deste valor, temos um total de {Calculos.aumentar(p, 10, True)}')
print(f'Diminuindo 20 % deste valor, temos um total de {Calculos.diminuir(p, 20, True)}')
