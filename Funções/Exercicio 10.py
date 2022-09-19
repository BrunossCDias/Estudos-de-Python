# Programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)


def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'APROVADO'
        elif r['média'] >= 5:
            r['situação'] = 'RECUPERAÇÃO'
        else:
            r['situação'] = 'REPROVADO'
    return r


boletim = notas(5.5, 6, 3.5, 4.5, 6, sit=True)
print(f'O aulo foi {boletim["situação"]}')
print(boletim)
print()
boletim = notas(5, sit=True)
print(boletim)