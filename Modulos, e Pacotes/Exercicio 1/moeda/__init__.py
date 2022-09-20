def aumentar(preço, taxa):
    calc = preço + (preço * taxa/100)
    return calc


def diminuir(preço, taxa):
    calc = preço - (preço * taxa/100)
    return calc


def dobro(preço):
    calc = preço * 2
    return calc

def metade(preço):
    calc = preço / 2
    return calc