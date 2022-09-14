# Programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


# Importando a biblioteca datetime apenas dentro da função.
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: O VOTO É OPCIONAL'
    else:
        return f'Com {idade} anos: O VOTO É OBRIGATORIO'

nasc = int(input('Em que você nasceu: '))
print(voto(nasc))
