
OQUE É ?

    Funções são trechos que podem ser executados em momentos diferentes do nossos códigos em Python. 
    Criamos uma função para obrtermos uma rotina de facil acesso, uma sequência de comandos que executa
    alguma tarefa e que tem um nome reservado. 
    A sua principal finalidade é nos ajudar a organizar programas em pedaços que correspondam a como imaginamos 
    uma solução do problema.
    Podemos explicitar os parametros do programa principal para mudar a ordem da função como desejar.

    Ex.
        def soma(a, b):
        print(f'A = {a} e B = {b}')
        s = a + b
        print(f'A soma A + B = {s}')

    # Programa principal
        soma(4, 5)
        soma(5, 5)
        soma(b=10, a=25)
    
    Em uma função podemos desempacotar uma determinada quantidade de parametros quando o seu programa começar a ficar em
    uma escala de tamanho maior.
    A instrução return nos permite que a função retorne um resultado que pode ser armazenado em uma variavel.
    


        