class Pessoa:
    def __init__(self, nome, idade, dirigindo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.dirigindo = dirigindo
        self.falando = falando

    def dirigir(self):
        if self.dirigindo:
            print(f'{self.nome}, já esta dirigindo.')
            return
        if self.falando:
            print(f'{self.nome} não pode dirigir falando no celular')
            return


        print(f'{self.nome} está dirigindo.')
        self.dirigindo = True

    def parardirigir(self):
        if not self.dirigindo:
            print(f'{self.nome} não esta dirigindo.')
            return
        else:
            print(f'{self.nome} parou de dirigir.')
            self.dirigindo = False

    def falar(self, assunto):
        if self.dirigindo:
            print(f'{self.nome} não pode falar no {assunto} dirigindo !')
            return
        if self.falando:
            print(f'{self.nome} ja está falando ! ')
            return

        print(f'{self.nome}, esta falando.')
        self.falando = True


    def pararfalar(self):
        if not self.falando:
            print(f'{self.nome}, não está falando.')
            return

        print(f'{self.nome}, parou de falar !!')

    def status(self):
        print(f'Dirigindo: {self.dirigindo}, Falando: {self.falando} ')