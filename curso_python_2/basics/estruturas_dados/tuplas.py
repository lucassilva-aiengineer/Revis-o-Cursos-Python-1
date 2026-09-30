# Tuplas
# Estruturas de dados ordenados, mutáveis e que aceitam elementos duplicados. 

def parte_1():

    minha_tupla = ("Marcos", 21, "Florianópolis")
    minha_tupla_1 = tuple(["Marcos", 25, "Goiânia"])

    print(minha_tupla)
    print(minha_tupla_1)

    # Acessando a tupla pelo índice 

    item = minha_tupla_1[0]

    print(item)

def parte_2():

    
    minha_tupla = ("Marcos", 21, "Florianópolis", "a", "a", "b", "b", "c")
    
    for i in minha_tupla:
        print(i)

    if "Marcos" in minha_tupla:
        print("sim")

    else:
        print("Não")

    print(len(minha_tupla))


    print(minha_tupla.count("a"))

    print(minha_tupla.index("a"))


def parte_3():

    minha_tupla = ("Marcos", 21, "Florianópolis", "a", "a", "b", "b", "c")

    minha_lista = list(minha_tupla)
    minha_lista.append("Mateus")

    print(minha_lista)


    minha_tupla = tuple(minha_lista)
    print(minha_tupla)




def parte_4():

    a = (1, 2, 3, 4, 5, 6, 7, 8)

    b = a[2: 6]
    c = a[::1]

    final = 7
    d = a[2:final:1]


    print(b)
    print(c)    


    tupla_a = "Marcos", "José", "João"

    print(tupla_a)

    nome_1, nome_2, nome_3 = tupla_a 

    print(nome_1)
    print(nome_2)
    print(nome_3)


def parte_5():

    minha_tupla = (1, 2, 3, 4, 5, 6)

    a, *b, c = minha_tupla

    print(a)
    print(b)
    print(c)


def parte_6():

    """
    Comparação: Listas VS Tuplas
    """

    import sys 
    minha_lista = [0, 1, 2, "Hello", True]
    minha_tupla = tuple([0, 1, 2, "Hello", True])

    print(sys.getsizeof(minha_lista), "bytes")
    print(sys.getsizeof(minha_tupla), "bytes")


    import timeit

    print(timeit.timeit(stmt= "[0, 1, 2, 3, 4, 5]", number= 1000000))
    print(timeit.timeit(stmt= "(0, 1, 2, 3, 4, 5)", number= 1000000))

def main():
    # parte_1()
    # parte_2()
    # parte_3()
    # parte_4()
    # parte_5()
    
    parte_6()



if __name__ == '__main__':
    main()