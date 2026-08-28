# Variáveis 

name = "Beau" ; print("Meu nome é Marcos!")

#   print("Indentação")

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
    ... 
    
def main():

    # verificar_str()
    # verificar_int()
    operadores_aritmericos()


if __name__ == '__main__':
    main()