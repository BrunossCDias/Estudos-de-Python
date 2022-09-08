#Imprima o salario de um funcionario com 15% de aumento.

salario = float (input('Salario atual R$ : '))
S_aumento = salario + (salario * 15 / 100)
print(f"Um funncionario que recebia R$ {salario}, com aumento de 15%, passará a receber R$ {S_aumento}")
