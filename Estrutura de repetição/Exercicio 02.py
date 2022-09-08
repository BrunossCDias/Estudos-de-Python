# Iteração com laço de repetição em uma estruta versatil com o FOR.

s = 0
for vezes in range(0, 4):
    valor = int(input('Digite um valaor: '))
    s += valor + 1
print(f'A soma de todos os valores é {s}')
print('\033[0;31;40mFIM ! \033[m')



inicio = int(input('Inicio : '))
fim = int(input('Fim : '))
passo = int(input('Passo :'))
for repetir in range (inicio, fim+1, passo ):
    print(repetir)

print('\033[0;31;40mFIM ! \033[m')