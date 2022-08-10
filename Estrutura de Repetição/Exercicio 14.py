# Programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um valor: '))
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > menor:
            maior = numero
        if numero < menor:
            menor = numero

    soma += numero
    quantidade += 1
    resposta = str(input( 'Deseja continuar [S/N]: ')).upper().strip()[0]
media = soma / quantidade
print(f'Você digitou {quantidade}, e a média entre eles é {media}')
print(f'O maior valor é {maior}, e o menor é {menor}')
print('Acabou')