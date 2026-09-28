# Funções lambda 

# Funções anônimas

# palavra_chave arg_a, arg_b : expressao 
# lambda a, b: a * b

# import numpy as np 
from typing import List, Tuple


# São funções muito utilizadas com argumento de funções maiores. 


def intr():
    lambda num : num * 10

    mult = lambda a, b : a * b

    print(mult(10, 2))



# map(), filter(), reduce()

# map()
# A função map() percorre um iterável, como lista, aplicando uma função, utilizando os itens como argumento. 

def funcao_map():
    lista = [1, 2, 3]

    def double(a):
        return a * 2

    # resultado = map(double, lista)

    resultado = map(lambda a : a * 2, lista)
    print(lista)
    print(list(resultado))


def funcao_filter():

    # lista_numeros = np.arange(0, 20)

    lista_numeros = list(range(10))

    def par(numero):
        return numero % 2 == 0 # Esta linha irá retornar o resultado desta avaliação True ou False 

        

    # A função integrada filter percorre uma lista, um iterável de elementos aplicando uma função que filtra valores, quando o elemento 
    # passa pelo filtro este elemento permanece na lista. 

    numeros_pares = filter(par, lista_numeros) 

    numeros_pares_a = filter(lambda numero: numero % 2 == 0, lista_numeros)
    print("Filtrando com a função lambda: " + str(list(numeros_pares_a)))

    # Tentando construir a minha própria função filter
    
    def meu_filter(funcao, elementos: List[int])-> List[int]:

        resultado: List[int] = []

        for valor in elementos:
            if funcao(valor):
                resultado += [valor]
    
            # continue  
            else:
                continue
                
        return resultado 
        # return [valor if funcao(valor) else continue for valor in valor]

    def testando_conceito():

        lista_inteiros = []

        lista_inteiros.append(10)

        lista_inteiros += [20]

        lista_inteiros += "String" # Adiciona como uma lista de carcteres, cadeia de caracteres, como se estivesse adicionando uma lista com letras separadas 
        # Seria algo como 

        lista_inteiros += ["Palavra 1", "Palavra 2"]

        lista_inteiros += ["string"]


        contagem_elemetos = 1
        for elemento in lista_inteiros:
            print(f"Elemento n° {contagem_elemetos}: {elemento}")
            contagem_elemetos += 1


    # funcao_filter()
    # testando_conceito()

    # elementos = [10, 12, 15, 14, 16, 20]
    # resultado = meu_filter(par, elementos)

    # print(resultado)

    print(list(numeros_pares))


def funcao_reduce():
    
    from functools import reduce 

    folha_pagamento = [
        ("Pedro", 2000),
        ("Marcos", 4000),
        ("José", 2000),
        ("Mateus", 10000) 
    ]

    gasto_total = sum([tupla[1] for tupla in folha_pagamento])

    print("Folha de pagamento: " + str(gasto_total))

    # Utilizando reduce
    # A função reduce, percorre um iterável em duplas 

    folha_total = reduce(lambda a, b: a + b[1], folha_pagamento, 0) 
    print("Resultado: ", folha_total)


def main():
    # intr()
    # funcao_filter()

    funcao_reduce()



if __name__ == '__main__':
    main()