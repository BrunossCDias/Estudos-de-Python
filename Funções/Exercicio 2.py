
# Programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.


def escreva(txt):
    tam = len(txt) + 4
    print('˜'*tam)
    print(f'  {txt}')
    print('˜'*tam)


escreva('Ola mundo !')
escreva('Cursando Pyhton Junior')
escreva('Hotmart')

''' Criei uma def chamada escreva com parametro chamado txt.
    Criei outra variavel identada a função chamada tam, que vai receber o len do parametro txt somando mais 4 indices. 
    Idetado a def, criei um print para uma impressão do simbolo tio, vezes a variavel tam
    criei mais um print formatado o paraentro txt com dois espaços no inicio para centralizar '''
