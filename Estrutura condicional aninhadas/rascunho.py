termo = int(input('Insira um termo: '))
razao = int(input('Insira uma razão da PA: '))
cont = 1
while cont <= 10:
    print(f'{termo}')
    termo += razao
    cont += 1
print('FIM')