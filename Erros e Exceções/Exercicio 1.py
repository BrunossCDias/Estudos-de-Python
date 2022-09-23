

from interface import *
from time import sleep

arq = 'cursopython.txt'

if not arqExiste(arq):
   criararquivo(arq)


cabecalho('Sistema de Cadastro v1.0')
while True:
    resposta = menu(['Cadastro de Pessoas', 'Consultar Cadastrados', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerarquivo(arq)
    elif resposta == 3:
        cabecalho('\033[36mSaindo do Sistema\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida !\033[m')
        sleep(2)
