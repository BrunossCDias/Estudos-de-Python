class Pessoa:
    sexo : str ='F/M'
    def __init__(self, nome, idade, dirigindo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.dirigindo = dirigindo
        self.falando = falando

    def dirigir(self, veiculo):
        if self.dirigindo:
            print(f'{self.nome}, já esta dirigindo.')
        else:
            print(f'{self.nome} está dirigindo o {veiculo}.')
            self.dirigindo = True

    def parardirigir(self, veiculo):
        if not self.dirigindo:
            print(f'{self.nome} não esta dirigindo {veiculo}.')

        else:
            print(f'{self.nome} parou de dirigir o {veiculo}.')
            self.dirigindo = False

    def falar(self, celular):

        if self.dirigindo:
            print(f'{self.nome} não pode falar no {celular} dirigindo !')
            return
        if self.falando:
            print(f'{self.nome} ja está falando no {celular} ! ')
            return

        print(f'{self.nome}, esta falando no {celular}.')
        self.falando = True

    def pararfalar(self, celular):
        if not self.falando:
            print(f'{self.nome}, não está falando no {celular}.')
            return
        print(f'{self.nome}, parou de falar no {celular} !!')
        self.falando = False

    def estado(self):

        return {'dirigindo': self.dirigindo, 'falando': self.falando}

    def verifica_estado(self, dirigindo , falando):
        validacao = (self.dirigindo == dirigindo and self.falando == falando)
        print(f'validacao: {validacao}')
        if (self.dirigindo == dirigindo and self.falando == falando ):
            return True
        return False




    # 1 Crie uma nova função que chama verifica_estado.
    # 2 Essa função deverá verificar se os parametros do estado esperado é igual o estado atual do objeto.
    # 3 Deverá retornar true quando for igual e false quando algum estado for diferente.


    ''' 
    def verifica_estado(self, dirigindo, falando) -> bool:
        if self.dirigindo == dirigindo and self.falando == falando:
            return True
        return False
    '''


    def imprime_estado(self):
      return print(f'Dirigindo: {self.dirigindo}, Falando: {self.falando} ')


