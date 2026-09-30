# Listas 
# Estruturas de dados ordenadas, mutáveis que aceitam elementos duplicados 

minha_lista = ["banana", "cereja", "maçã"]
print(minha_lista)


def parte_1():
    minha_lista_2 = [True, False, "Maçã"]
    print(minha_lista_2)

    item = minha_lista_2[0]
    print(item)


    item_3 = minha_lista[-1]
    print(item_3)


    for elemento in minha_lista:
        print(minha_lista)


    if "banana" in minha_lista:
        print("Sim!")

    else:
        print("Não!")


def parte_2():

    minha_lista = ["Mateus", "José", "Lucas"]
    print(len(minha_lista))

    minha_lista.append("novo_elemento")
    print(minha_lista)

    minha_lista.insert(2, "João")
    print(minha_lista)

    item_removido = minha_lista.pop()
    print(item_removido)

    minha_lista.remove("João")

    print(minha_lista)

    # lista = minha_lista.clear() # Removendo todos os elementos 

    # print(lista)

    lista_ordenada = minha_lista.sort()
    print(minha_lista)

    nova_lista = sorted(minha_lista, reverse= True) # não altera a lista origina 
    print(nova_lista)

    lista_zeros = [0] * 10

    print(lista_zeros)

    nova_lista_2 = lista_zeros + minha_lista

    print(nova_lista_2)

def parte_3():

    # Fatiamento 
    # Acessando partes da lista por meio de ":"

    minha_lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    a = minha_lista_a[0: 4]
    b = minha_lista_a[:4]
    c = minha_lista_a[5:]

    d = minha_lista_a[:: 2] # Índice inicial até ao índice final 
    e = minha_lista_a[:: -1] # revertando a lista / Só existe índice anterior se inicia pelo fim. 

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)


    # Cópias 

    lista_original = ["maça", "banana", "laranja"]

    copia_real = list(lista_original)
    copia_real_1 = lista_original[:]

    copia_real_2 = lista_original.copy()

    lista_copia = lista_original
    lista_copia.append("Adicionando elemento a copia fake")

    copia_real_2.append("teste")

    print(lista_original)
    print(copia_real_1)
    print(copia_real_2)

    print(lista_copia)


def parte_4():

    # list compression 
    a = [1, 2, 3, 4, 5, 6]

    b = [i + 5 for i in a]
    print(b)

def main():

    # parte_2()
    # parte_3()
    parte_4()


if __name__ == '__main__':
    main()