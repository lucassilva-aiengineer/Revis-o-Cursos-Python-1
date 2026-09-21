# Conjuntos
# São bem parecidos com listas, porém não são ordenados e não permitem duplicadas, são mutáveis. 
# Há uma versão de conjuntos imutável chamada frozenset()


def conjuntos_a():

    conjunto_1 = {
        "Marcos", "José", "Mateus", "João", "Lucas"
    }

    conjunto_2 = {
        "Marcos", "José", "Mateus", "João"
    }

    intersect = conjunto_1 & conjunto_2

    # A interseção dos dois conjuntos, o que está tanto em um quanto em outro. 

    # print(conjunto_1) 

    print(f"Intersect: {intersect}")

    disjuncao = conjunto_1 | conjunto_2 

    # Aquilo que está tanto no conjunto A quanto no conjunto B, os elementos que fazem parte ou de um conjunto ou de outro. 
    print(f"Disjunção: {disjuncao}")

    
    # Diferença de conjuntos 
    diferenca = conjunto_1 - conjunto_2
    print(diferenca)

    maior = conjunto_1 >= conjunto_2    
    menor_que = conjunto_1 < conjunto_2 


    print(f"O conjunto 1 é maior que o conjunto 2: {maior}")

    print(f"O conjunto 1 é menor que o conjunto dois: {menor_que}")

    print(len(conjunto_1))

    conjunto = {10, 10, 10, "Lucas", "Mateus", "Marcos", "Marcos"}

    print(list(conjunto_1))
    print(f"Os conjuntos não permitem elementos duplicados {conjunto}")

def main():


    # ... 
    conjuntos_a()


if __name__ == '__main__':
    main()