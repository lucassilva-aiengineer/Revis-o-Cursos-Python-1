
def funcao_product():
    from itertools import product 

    a = [1, 2]
    b = [3, 4]

    prod = product(a, b)
    print(list(prod))

    prod_a = product(a, b, repeat= 2)
    print(list(prod_a))


def funcao_permutations():
    from itertools import permutations 


    a = [1, 2, 3]

    # Criamos uma lista com todas as permutações possíveis de uma lista. 
    # perm = permutations(a)
    perm = permutations(a, 2) # Regulando o tamanho das permutações

    # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    print(list(perm))



def funcao_combinations():

    from itertools import combinations, combinations_with_replacement
    lista = [1, 2, 3, 4]

    combinacoes = combinations(lista, 2)
    print(list(combinacoes))

    print("Combinações com repetições: ")
    combinacoes_com_repeticoes = combinations_with_replacement(lista, 2)

    print(list(combinacoes_com_repeticoes))


import operator 

def funcao_accumulate():

    from itertools import accumulate 

    lista = [1, 2, 3, 4, 5]
    somas_acumuladas = accumulate(lista)

    produtos_acumulados = accumulate(lista, func= operator.mul)
    # produtos_acumulados = accumulate(lista, func= max)


    print("Valor valor de soma acumulado: ")
    print(lista)
    print(list(somas_acumuladas))

    for valor in lista:
        print(valor)
    
    print("\n")
    print("Produto acumulado dos valores: {}".format(list(produtos_acumulados)))



def funcao_groupby():
    from itertools import groupby


    def menor_que(numero):
        return numero < 3

    
    def situacao_1():
        
        lista = [1, 2, 3, 4]
        # objeto_grupo = groupby(lista, key= menor_que) # Filtra a lista retornando apenas os valhores menores que o valor 3 

        objeto_grupo = groupby(lista, key= lambda x: x < 3) # Filtra a lista retornando apenas os valhores menores que o valor 3 

        # print(list(objeto_grupo))

        for chave, valor in objeto_grupo:
            print(chave, list(valor))


    def situacao_2():

        pessoas = [
            {
            "nome": "Marcos",
            "salario": 10000
            },
            {
                "nome": "Mateus",
                "salario": 10000
            },
            {
                "nome": "José",
                "salario": 12000
            }
            ]


        grupos = groupby(pessoas, key= lambda x: x['salario'])

        for chave, valor in grupos:
            print(chave, list(valor))


    # situacao_2() 
    
    def situacao_3():
        from itertools import count, cycle, repeat 

        for i in count(10):
            print(i)


            if i == 15:
                print("15 encontrado!")
                print(i)
                break 

    situacao_3()

def main():

    # funcao_permutations()
    # funcao_combinations()

    # funcao_accumulate()
    funcao_groupby()


if __name__ == '__main__':
    main()


