    
    Uma representação de itens fisicos, ideias ou conceitos abstratos do mundo real um paradigma orientado a objeto,
        forma de escrever uma programação orientada a objeto, criando CLASSES para definir uma ordem para os objetos, 
        em toda CLASSE deve possuir um metodo __init__ com as caracteristicas do objeto, e um parametro SELF um refer_
        enciar as instancia da CLASSE.
    Por convenção, iniciamos o nome de uma CLASSE com caractere maiusculo, e capitalizamos cada pavra subsequente do 
        nome,  utilizando a conveção de nomeação PascalCase
    
      Ex.  Class Cubo:
                def __init__(self, valor)
                self.x = valor
                print ('Obejto criado')
                

                def calcula(self):
                    cubo = self.x * 3
                    return 'Cubo calculado str(cubo)

    Vantagem de uma classe é pode ter um programa modulirazado em partes menores, facil de manter o programa, e o reuso
        do seu codigo.

    Métodos é utilizado para atribuir comportamento ao objeto, são similares a funções e procedimentos, o ato de chamar
        ou invocar um metodo, é a passagem de mensagem para o objeto.

    Metodos estaticos não precisam de uma referência, não recebem um primeiro argumento especial (self). 
    É como uma função simples que, por acaso, reside no corpo de uma classe em vez de ser definida no nível do módulo.
    
    Henraça é o relacinamento, podendo assim criar uma classe com atributos e metodos de outra classe, evitando se assim
        uma repetição de codito.

    Encapsulamento 

    Polismorfismo são muitas formas do objeto, dependendo de como ele é chamado, e seus atributos podendo retornar funci
        onalidades diferentes ou comportamentos distintos