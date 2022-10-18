from Classes import Pessoa

motorista = Pessoa('Luiz', 39)
print(motorista.sexo)
motorista.dirigir('carro')
motorista.falar('celular')
motorista.parardirigir('carro')
motorista.falar('celular')
motorista.pararfalar('celular')
motorista.dirigir('caminhao')
motorista.dirigir('carro')
motorista.falar('WhatsApp')
motorista.parardirigir('caminhão')













# 1 Verificar o estado do objeto
# 2 Verificar cada possibilidade
motorista.falar('Celular')
motorista.dirigir('Carro')
motorista.estado()
motorista.verifica_estado(False, True)
motorista.verifica_estado(True, False)
motorista.verifica_estado(True, True)
motorista.verifica_estado(False, False)
motorista.parardirigir('Carro')
motorista.pararfalar('Celular')
motorista.estado()
motorista.verifica_estado(False, True)
motorista.verifica_estado(True, False)
motorista.verifica_estado(True, True)
motorista.verifica_estado(False, False)
motorista.dirigir('Carro')
motorista.pararfalar('Celular')
motorista.estado()
motorista.verifica_estado(False, True)
motorista.verifica_estado(True, False)
motorista.verifica_estado(True, True)
motorista.verifica_estado(False, False)
motorista.parardirigir('Carro')
motorista.falar('Celular')
motorista.estado()
motorista.verifica_estado(False, True)
motorista.verifica_estado(True, False)
motorista.verifica_estado(True, True)
motorista.verifica_estado(False, False)


