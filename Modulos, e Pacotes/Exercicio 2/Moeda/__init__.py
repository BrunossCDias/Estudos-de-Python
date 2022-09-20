def aumentar(preço=0, taxa=0):
    calc = preço + (preço * taxa/100)
    return calc


def diminuir(preço=0, taxa=0):
    calc = preço - (preço * taxa/100)
    return calc


def dobro(preço=0):
    calc = preço * 2
    return calc

def metade(preço=0):
    calc = preço / 2
    return calc


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')