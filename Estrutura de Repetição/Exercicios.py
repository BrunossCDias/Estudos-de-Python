

nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
else:
     print("Todos os nomes foram listados com sucesso")


#Exercicios

print('Exercicio 1')

# Iteração com laço de repetição em uma estruta versatil com o FOR.


s = 0
for vezes in range(0, 4):
    valor = int(input('Digite um valaor: '))
    s += valor + 1
print('A soma de todos os valores é {}'.format(s))
print('\033[0;31;40mFIM ! \033[m')



inicio = int(input('Inicio : '))
fim = int(input('Fim : '))
passo = int(input('Passo :'))
for repetir in range (inicio, fim+1, passo ):
    print(repetir)

print('\033[0;31;40mFIM ! \033[m')

#Exercicios

print('Exercicio 2')
#Programa que faça uma contagem regressiva de 10 até 0.

from time import sleep
for regressao in range(10, -1, -1):
    sleep(1)
    print(regressao)

   
print('Exercicio 2')
# Programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.
soma = 0
contador = 0
for impares in range(1, 501, 2):
    if impares % 3 == 0:
        soma += impares
        contador += 1
print('A soma de todos os {} numero impares multiplos de 3 é {}'.format(contador, soma))
 #ou
s = c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        c += 1
        s += n
print(f"A soma de todos os {c} valores solicitados é {s}.")


print('Exercicio 3')
#programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

contador1 = 0
somador = 0
for repetir in range (1, 7):
    numero2 = int(input('Digite o {}˚ valor: '.format(repetir)))
    if numero2 % 2 == 0:
        somador += numero2
        contador1 += 1
print('Voce informou {} numeros PAERES, e a soma de todos eles é {}'.format(contador1, somador))
