
num = [1, 2, 0, 4]
print(num)
num.insert(3, 5)
print(num)
num[2] = 6
num.append(9)
print(num)
num.sort()
print(num)
num.append(34)
num.append('banana')
num.insert(0, 'suco')
print(num)
num.remove('suco')
del num[3]
print(num)
num.pop()
if 'banana' in num:
    num.remove('banana')
else:
    print('Indice não encontrado')
print(num)

num.append(22)
num.append(23)
num.append(25)
num.sort()
for indice, numero in enumerate(num):
    print(f'No indice {indice}  encontrei o valor {numero} !')
print('FIM DA LISTA.')