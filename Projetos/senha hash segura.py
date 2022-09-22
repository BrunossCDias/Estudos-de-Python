import bcrypt
from time import sleep

senha = b"234234345"
incremento = bcrypt.gensalt()
hash = (bcrypt.hashpw(senha, incremento))
print(f'Criptogranfando....\n{(hash)}')
print('=-'*20)
print('Verificando sua senha.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
print('-'*20)

if bcrypt.checkpw(senha, hash):
    print('Autorizado')
else:
    print('Negado')