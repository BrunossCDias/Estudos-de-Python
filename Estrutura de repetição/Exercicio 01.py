
# Programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0:
        soma += impares
        contador += 1
print(f'A soma de todos os {contador} numero impares multiplos de 3 é {soma}')
 #ou
s = c = 0
for n in range(1, 501, 2): #
    if n % 3 == 0:
        c += 1
        s += n
print(f"A soma de todos os {c} valores solicitados é {s}.")
















