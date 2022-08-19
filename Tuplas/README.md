* OQUE É ?
    
    Em Python, as tuplas são muitos semelhantes às listas, no entanto, ao contratrario das listas,
elas são imutáveis, oque significa que não podem ser alteradas, pode-se usar tuplas para apresen
tar coisas que não deveriam ser alteradas.

Exemplo: 
        Podemos determinar os elementos que serão impressos através da manipulação, e fatiamento.
        
        carro = ('pneu', 'amortecedores', 'freios', 'farois', 'coxins')
        
        print(carro[1:3])
        
        print(carro[:2])
        
        print(carro[-1:]) 
        
Posso também detalhar os elementos da tupla dentro de uma iteração com FOR. 
    
    FOR revisao IN carro:
        
        print(f'Eu vou fazer uma revisão nos {revisao} do carro.')
    
    FOR revisao in RANGE(0, len(carro)):

        print(f'Eu vou fazer uma revisão nos {carro[revisao]} do carro.')
