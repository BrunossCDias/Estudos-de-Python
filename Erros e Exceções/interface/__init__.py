import keyword

def leiafloat (msgem):
    while True:
        try:
            m = float(input(msgem))
        except (ValueError, TypeError):
            print('\033[31mErro : Por Favor digite um valor float valido.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar um valor numerico.\033[m')
            return 0
        else:
            return m


def leiaint (msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: Por Favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario preferiu não digitar um valor numerico.\033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('SELECIONE UMA OPCÃO')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    opc = leiaint('\033[32mSua opção : \033[m')
    return opc
