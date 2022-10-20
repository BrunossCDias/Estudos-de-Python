

expre = str(input('Digite sua expressão: '))
acumulador = list()

for s in expre:
    if s == '(':
        acumulador.append('(')
    elif s == ')':
        if len(acumulador) > 0:
            acumulador.pop()
        else:
            acumulador.append(')')
            break
if len(acumulador) == 0:
    print('Esta expressão é válida !')
else:
    print('Esta expressão está errada !')

''' Variavel EXPRE recebe através do teclado uma expressao.
    Definido uma variavel ACUMULADOR como uma lista.
    Criado um loop FOR para varrer os indices da variavel EXPRE. 
    Um IF para verificar se o indice é um parentese abrindo, e adiciona-lo ao acumulador.
    Um ELIF para verificar se o indice é um parentese fechando.
    Um IF verificando com um metodo LEN se o tamanho do acumulador é maior que 0.
    Se for maior que 0, é removido do acumulador o ultimo indice com a função POP.
    Um ELSE caso o acumular esteja com 0 indices, é adicionado com um append, o parentese a variavel acumulador.
    No fim defino uma condição IF para saber se o LEN de acumulador é igual a 0, e imprimo como uma exopressão valida.
    Se ELSE não for igual a 0, imprimo como uma expressão errada. '''