* OQUE É ?
    
    Em Python, as tuplas são muitos semelhantes às listas, no entanto, ao contratrario das listas,
elas são imutáveis, oque significa que não podem ser alteradas, pode-se usar tuplas para apresen
tar coisas que não deveriam ser alteradas.

Exemplo: 
        Podemos determinar os elementos que serão impressos através da manipulação, e fatiamento.
        
        carro = ('pneu', 'motor', 'freios', 'farois')
        
        print(carro[1:3])
        
        print(carro[:2])
        
        print(carro[-1:]) 
        
Podemos tambem detalhar os elementos da tupla dentro de uma repetição FOR. 
    
    FOR revisao IN carro:
        
        print(f'Eu vou fazer uma revisão no {} do meu carro.')
           
        
