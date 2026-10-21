# Funções Lambda 


# adicao = lambda arg1, arg2: expressao  

adicao = lambda a, b: a + b

print(adicao(10, 5))


def multiplicacao(a, b):
    return a * b 



print(multiplicacao(10, 10))


# As funções lambda são muito úteis como argumentos de métodos
def argumentos_lamb():


    # def ordene

    elementos = [(1, 2), (15, 1), (5, -1), (10, 5)]

    elementos_ordenados_1 = sorted(elementos) 
    elementos_ordenados_2 = sorted(elementos, key= lambda tupla: tupla[1], reverse= True) 


    # ordenando pela soma dos elementos que compõe a tupla 
    elementos_ordenados_3 = sorted(elementos, key= lambda tupla: tupla[0] + tupla[1])

    # print(elementos_ordenados_2)
    print(elementos_ordenados_3)



def funcoes_integradas():

    lista_numeros = [numero for numero in range(10)]
    lista_2 = map(lambda n: n * 2, lista_numeros)


    print("Lista Original:")
    print(lista_numeros)
    print("\nLista Multiplicada Por 2:")
    print(list(lista_2))


    # Utilizando uma sintaxe mais simples 
    numeros = [a * 2 for a in lista_numeros]
    print("\nResultados Mais Simples: ")
    print(list(numeros))


    valores_filtrados = filter(lambda n: n % 2 == 0, lista_numeros)
    print(list(valores_filtrados))


    # Calculando o produtos 
    from functools import reduce 

    numeros = [10, 20, 30, 40, 50]
    produtos = reduce(lambda x, y: x * y, numeros)

    print(produtos)

def main():

    # argumentos_lamb()
    funcoes_integradas()


if __name__ == '__main__':
    main()