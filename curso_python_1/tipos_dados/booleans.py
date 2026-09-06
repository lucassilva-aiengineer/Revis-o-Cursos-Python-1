# Valores booleanos 

from typing import List


def exemplo_1()-> None:

    """
        Um exemplo de estrutura de condicional que 
        executa uma instrução quando uma condição é 
        avaliada como sendo verdadeira.
    """

    feito = True

    if feito == True:
        print("O serviço foi realizado com sucesso!")

    else:
        print("O serviço não foi realizado com sucesso!")



def exemplo_2()-> None:

    feito = True
    if feito:
        print("O serviço foi realizado com sucesso!")

    else:
        print("O serviço não foi realizado com sucesso!")



# A maioria dos objetos são avaliados como sendo verdadeiros 

def exemplo_3()-> None: 

    valor = -5 

    print("\nPrimeira condição \n")
    if valor:
        print("Valor avaliado como verdadeiro")

    else:
        print("Valor avaliado como falso")


    valor_1 = 0

    print("\nSegunda condição \n")
    if valor:
        print("Valor avaliado como falso")

    else:
        print("Valor avaliado como verdadeiro")


    # As estruturas de dados vazias (listas, tuplas, dicionários e etc) são sempre avaliadas como falsas.  
    
    valor_2: List[int] = []

    print("\nTerceira condição: \n")
    if not valor_2:
        print("Valor avaliado como não verdadeiro!")

    else:
        print("Valor avaliado como verdadeiro!")

    valor_3 = ""

    if valor_3:
        print("O valor três é verdadeiro")

    else:
        print("O valor três é considerado falso")

    
    if ():
        print("Estrutura de dados vazia considerada como verdadeira!")

    else:
        print("Estrutura de dados considerada como falsa!")

    
    variavel = True
    print("\n", type(valor) == bool)
    print("Qual o tipo de dados da variável é um booleano: " + str(type(variavel) == bool) )


    print("Esta variável uma instância (objeto) desta classe: ", isinstance(variavel, bool))

    numero_inteiro = 10
    print("Este número inteiro é uma instância de int {}".format("Sim" if  isinstance(numero_inteiro, int) else "Não"))

# Algumas funções importantes

def funcoes_integradas():

    valor_1 = True 
    valor_2 = True

    valores = [valor_1, valor_2] 

    # Verifica se há algum valor verdadeiro na lista, vetor. 
    verificar = any(valores)
    print(f"Há algum valor True na lista: {verificar}")


    # Verificar se todos os valores em um vetor (lista) são verdadeiros 

    verificar_2 = all(valores)

    print("Todos os valores da lista são verdadeiros: " + str(verificar_2))

def main()-> None: 

    # exemplo_3()

    funcoes_integradas()

if __name__ == '__main__':
    main()