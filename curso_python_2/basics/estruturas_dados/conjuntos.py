
# Conjunto
# Estruturas de dados desordenadas, mutéveis que não aceitam elementos duplicados, são muito parecidas com as listas, sendo guardadas as exceções. 


def conjunto_1():
    conjunto = {1, 2, 3, 1, 2}
    print(conjunto)

    conjunto_1 = set((1, 2, 3, 4))
    print(conjunto_1)


    # Adicionando elementos 

    conjunto.add(10)
    conjunto.add(30)
    conjunto.add(50)

    conjunto.remove(10)

    print(conjunto)


    # O método discard
    # Quando o elemento que se propõe não é encontrado tem-se um erro 
    conjunto.discard(15)

    print(conjunto)

    # Esvasiando o conjunto inteiro. 

    conjunto.clear()

    conjunto.add(100)
    conjunto.add(200)
    conjunto.add(300)

    conjunto.pop() # Resmovendo um elemento Arbitráriamente

    print(conjunto)


def conjunto_2():
    
    conjunto = {10, 20, 50, 30, 100}

    for i in conjunto:
        print(i)

    if 10 in conjunto:
        print("sim")

    else:
        print("Não")



def conjunto_3():

    # União e Intercessão 

    impares = {1, 3, 5, 7, 9}
    pares = {2, 4, 6, 8, 10}
    primos = {2, 3, 5, 7}

    # União os elementos que estam no conjunto A ou estam no conjunto B 
    u = impares.union(pares) 
    print(f"União do conjunto A e do Conjunto B: {u}")

    # Intercection - Os elementos 
    i = impares.intersection(primos)
    print(f"Interceção do conjunto de pares com impares {i}")


    # Calculaculando a diferença entre os dois conjuntos 


    conjunto_A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    conjunto_B = {1, 2, 3, 10, 11, 12}

    diferenca = conjunto_A - conjunto_B
    print(diferenca)


    diff = conjunto_A.difference(conjunto_B)

    # Diferença 
    print(diff)

    # Diferença simétrica 
    
    diferenca_simetrica = conjunto_B.symmetric_difference(conjunto_A)
    diferenca_simetrica2 = conjunto_A.symmetric_difference(conjunto_B)

    print(diferenca_simetrica2)

    # x + y - (y + z)
    # x + y - y - z
    # x - z 

    # Atualização de conjuntos  
    conjunto_A.update(conjunto_B) # Agora conjunto A passa a ter todos os elementos de B
    print(conjunto_A)

    conjunto_B.update(conjunto_A) # Agora o conjunto B passa a ter todos os elementos de A
    print(conjunto_B)


def conjunto_4():

    conjunto_A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    conjunto_B = {1, 2, 3, 10, 11, 12}

    print(conjunto_A.issubset(conjunto_B)) # O conjunto B é um sub conjunto de A
    print("B é um subconjunto de A " + str(conjunto_B.issubset(conjunto_A)))
    

    # Super conjunto 
    print(conjunto_A.issuperset(conjunto_B)) # A é um superconjunto de B

    # Verficando uma disjunção 
    # Se dois conjuntos não possuem elementos em comum 

    print("A e B conjuntos disjuntos: ")
    print(conjunto_A.isdisjoint(conjunto_B))


def conjunto_5():

    conjunto_A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    # conjunto_B = {1, 2, 3, 10, 11, 12}

    # Cópias Reais 

    copia_1 = conjunto_A.copy() 
    copia_1.add(30)

    print("Cópia 1")
    print(copia_1)

    copia_2 = set(conjunto_A)
    copia_2.add(40)

    print("\nCópia 2")
    print(copia_2)

    print("\nConjunto Original")
    print(conjunto_A)

    conjunto_A.remove(9)
    print(conjunto_A)

    
def main():

    # conjunto_1() 
    # conjunto_2()
    # conjunto_3()
    # conjunto_4()
    conjunto_5()

if __name__ == '__main__':
    main()