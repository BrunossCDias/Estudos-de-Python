#Imprima quantos dolares pode ser comprado com uma quantidade em reais.

real = float(input('Insira um valor ? R$ '))
dolar = real / 5.48
print(f'Com R${real:.2f} é possivel comprar  U${dolar:.2f} dolares')
