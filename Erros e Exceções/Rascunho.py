try:
    a = int(input('Digite um valor: '))
    b = int(input('Digite mais um valor: '))
    c = a / b
    print(c)

    # Tipo de error.
except (TypeError, ValueError):
    print(f'Infelizmente existe um problema com o tipo de dados inserido ')
except ZeroDivisionError:
    print('Não é possivel dividir por zero !')
except KeyboardInterrupt:
    print('\nO usuario decidiu encerrar o programa !')
except Exception as erro:
    print(f'Ocorreu um {erro.__cause__} inesperado')
else:
    print(f'O resultado é {c:.1f}')
finally:
    print('Volte sempre, Obrg....')
