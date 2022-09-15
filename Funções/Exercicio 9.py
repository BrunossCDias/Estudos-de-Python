# Programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que
# fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leianum(msg):
    """

    """
    ok = False
    n = 0
    while True:
        valor = str(input(msg))
        if valor.isnumeric():
            n = int(valor)
            ok = True
        else:
            print('\033[0;31mErro, digite um valor númerico !\033[m')
        if ok:
            break
    return n


valor = leianum('Digite um número: ')
print(f'Você acabou de digitar o valor {valor}')
