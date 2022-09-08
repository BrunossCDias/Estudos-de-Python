# Imprima a quatidade de tinta suficiente para pintar um determinada medida de parede, sabendo que 2l de tinta
#pinta uma area de 2m

largura = float(input('Qual a largura da parede ? '))
altura = float(input('Qual a altura da parede ? ' ))
area = largura * altura
print(f'Sua parede tem a dimensao de {largura} x {altura} e sua area é de {area}m.')
litros = area /2
print(f'Para pintar essa parede, vai ser necessario uma quantidade de {litros}l de tinta.')
