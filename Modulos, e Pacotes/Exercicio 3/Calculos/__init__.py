def aumentar(preço=0, taxa=0, formato=False):
    """
    @param preço: Valor a ser feito o cálculo.
    @param taxa: Parametro que identifica o valor da taxa de aumento.
    @param formato: Formatando para a moeda local com virgula e casas decimais.
    @return: Resultado do calculo matematico.
    """
    calc = preço + (preço * taxa/100)
    return calc if format is True else moeda(calc)


def diminuir(preço=0, taxa=0, formato=False):
    calc = preço - (preço * taxa/100)
    return calc if formato is False else moeda(calc)


def dobro(preço=0, formato=False):
    calc = preço * 2
    return calc if not formato else moeda(calc)

def metade(preço=0, formato=False):
    calc = preço / 2
    return calc if not formato else moeda(calc)


def moeda(preço=0, moeda='R$'):
    """
    @param preço:
    @param moeda: ParametroSTR do formato da moeda local
    @return: Uma STR formatada com duas casas decimais, com um metodo replace
    """
    return f'{moeda}{preço:.2f}'.replace('.', ',')


