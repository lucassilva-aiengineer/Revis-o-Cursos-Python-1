# Variáveis 

def variaveis():

    name = "Beau" ; print("Meu nome é Marcos!")

    print("Indentação")

# Indica o escopo de um bloco de código.

# Tipos de dados 

def verificar_str():
    name = "Mateus" 
    print(type(name))

    print(type(name) == True)

    print(isinstance(name, str))

def verificar_int():
    age = 10

    print(type(age))
    print(type(age) == int)

    print(isinstance(age, int))


    age = float(10)
    print(isinstance(age, float))

    idade = "20"

    # Type casting mudar os tipos de dados 
    # atravez do construtor. 


    print("Idade é uma string?")
    print(isinstance(idade, str))

# Operadores 
# Elementos da sintaxe que realizão operações 

def operadores_a():

    # Operador de atribuição 
    # Atribui um valor, um espaço na memória alocado, a um nome, quando chamamos a variável
    # chamamos o valor alocado no espaço de memória. 

    a = 10 


# Operadores aritmáticos 
def operadores_aritmericos():
    """
        Operadores aritméticos, 
        Contas mais princípais. 
    """

    adicao = 1 + 1 # Também utilizamos para concatenar strings, textos. 

    # Também podemos utilizar o sinal de adição para encrementar valores 
    subtracao = 1 - 1 
    mult = 1 * 2 
    div = 10 / 2 

    resto_divisao_inteira = 10 % 2  # Quando o resto é diferente de zero temos uma divisão não inteira / não exata. 
    # Sem casas decimais 

    potenciacao = 10 ** 2 

    # Resultado da divisão inteira, quosciente. 
    divisao_inteira = 5 // 2
    print(divisao_inteira) # Dois  

    valor = 100
    valor = valor + 1

    valor_a = 1
    print("Valor A: {}".format(valor_a))
    valor_a += 1

    print("Valor A: {}".format(valor_a))

    # Também podemos multiplicar 

    a = 10 
    a = a * 10 
    a *= 10 

    print(a)

    # Decrementando 
    a_1 = 10 
    a_1 -= 1 

    for n in range(4):
        a_1 -= 1

    print("Após decrementarmos: " + str(a_1))

# Deus tem uma vida boa para mim. 



# Operadores de comparação 
def operadores_comparacao():

    a = 1 
    b = 2 

    a == b # Igual
    a != b # Não igual  
    
    a > b # Maior que 
    a >= b # Maior ou igual 

    a < b # Maior que 
    a <= b # Menor ou que
    


def operadores_logicos():

    def parte_1():
        condicao_1 = True
        condicao_2 = False 

        print(not condicao_1) 

        print("\nFalse", condicao_1 and condicao_2)
        print("\nTrue", condicao_1 and not condicao_2)

        print("\nTrue", condicao_1 or condicao_2)
        print("\nFalse", not condicao_1 or condicao_2)


    def parte_2()->None:

        """
            Um fato interessante dos operadores lógicos 
        """

        print(0 or 1) # 1 Retorna a primeira proposição, não sendo esta falsa.
        print(1 or 0) # 1 
        print(1 or 2) # 1 

        print([] or False) # Caso as duas proposições sejam falsas a última é retornada. 
    

        
    def parte_3()->None:


        print(0 and 1) ## 0, Retorna o segundo argumento somente quando o primeiro é verdadeiro
        print(1 and 0) ## 0 

        print(False and 'hey')  # False, retorna o segundo argumento apenas quando o primeiro é verdadeiro caso 
                                # Caso contrário sempre retorna o primeiro. 

        print([] and True) # []

        print(True and False)

    parte_3()


def operadores_bitwise():
    ... 

def main():

    # verificar_str()
    # verificar_int()
    operadores_logicos()


if __name__ == '__main__':
    main()