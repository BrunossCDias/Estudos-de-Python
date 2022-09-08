#programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

contador1 = 0
somador = 0
for repetir in range (1, 7):
    numero2 = int(input(f'Digite o {repetir}˚ valor: '))
    if numero2 % 2 == 0:
        somador += numero2
        contador1 += 1
print(f'Voce informou {contador1} numeros PAERES, e a soma de todos eles é {somador}')