# Programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str (input('Informe o seu SEXO : [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos ! Por Favor informe seu SEXO:  ')).strip().upper()
print(f'O seu sexo {sexo} foi registrado com sucesso. ')
