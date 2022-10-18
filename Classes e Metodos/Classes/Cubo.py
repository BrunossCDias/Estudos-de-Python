class Cubo:
    def __init__(self, valor):
        self.x = valor
        print('Obejto criado')

    def calcula(self):
        cubo = self.x * self.x * self.x
        return 'Cubo calculado : ' + str(cubo)



