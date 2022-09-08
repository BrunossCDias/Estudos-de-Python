# Programa que faça uma contagem regressiva de 10 até 0.

from time import sleep

for regressao in range(10, -1, -1):
    sleep(1)
    print(regressao)
