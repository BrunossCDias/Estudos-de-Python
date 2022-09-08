#imprima o valor do produto com 5% de desconto.

preco = float (input('Valor do produto? R$: '))
desconto = preco - (preco * 5/ 100)
print(f'O valor a ser pago com desconto de 5% é R${desconto}')