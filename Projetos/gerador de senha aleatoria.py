import random

maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculo = "abcdefghijklmnopqrstuvwxyz"
numeros = "1234567890"
especiais = ".+-[]*~_@#:?"
combinacao = maiusculo + minusculo + numeros + especiais
tamanho = 10
senha = "".join(random.sample(combinacao, tamanho))
print(f'A nova senha gerada é : {senha}')