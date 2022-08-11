# Programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato.

print('CASAS MARIA')

contador = totalg = menorp = m1000 = 0
barato = ''
while True:
    produto = (str(input('Oque deseja comprar ? ')))
    preço = float(input('Preço R$: '))
    totalg += preço
    contador += 1

    if preço > 1000:
        m1000 += 1
    if contador == 1 or preço < menorp:
        menorp = preço
        barato = produto
    resposta = ' '
    while resposta not in 'S/N':
        resposta = str(input('Quer continuar comprando ? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'Total da sua compra é de R$: {totalg:.2f}')
print(f'{m1000} produto"s estão acima de R$1.000,00')
print(f'O produto mais barato foi {barato}, e custou R$ {menorp:.2f}')
print('Volte sempre !')


''' DEFINIMOS VARIAVEIS COM VALORES EM 0, E ESPAÇO VAZIO.
    INICIAMOS UM LOOPIN INFINITO ENQUANTO FOR VERDADEIRO.
    É INSERIDO O NOME DO PRODUTO E O VALOR ATRAVÉS DO TECLADO.
    É FEITA A SOMA DAS VARIAVEIS TOTAL GASTO E PREÇO,  O CONTADOR E VALOR.
    SE O PREÇO FOR MENOR QUE 1000 A VARIAL MENOS DE 1000$ SOMA ELA MESMA MAIS 1
    SE O CONTADOR FOR O PRIMEIRO LOOPIN 'ou' O PREÇO FOR MENOR QUE O MENOR PREÇO
    AS VARIAVEIS MENOR PREÇO RECEBE PREÇO, E BARATO RECEBE  PRODUTO
    A VARIAVEL RESPOSTA RECEBE VAZIO
    DEFINIMOS UM LOOPIN ENQUANTO A VARIAVEL RESPOSTA NÁO RECEBER OS VALORES S/N 
    VARIAVEL RESPOSTA E INSERIDA ATRAVES DO TECLADO COMO UMA STRING, FORMATANDO EM MAIUSCULAM E SEM
        ESPAÇOS, SENDO LIDO APENAS O PRIMEIRO CARACTER.
  AGORA SE A VARIAVEL RESPOSTA RECEBER 'N' É REALIZADO UMA PARA NO LAÇO.'''