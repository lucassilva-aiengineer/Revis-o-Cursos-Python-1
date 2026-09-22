# Loop For 

# Laço de repetição 


# O loop for se trata de um iterador ele percorre estruturas de dados, listas, strings, dicionários, conjuntos, tuplas etc... 
# executando uma instrução, um bloco de código, ele realiza instruções finitas, tendo sempre predeterminada uma quantidade de execuções que 
# seram realizadas.


def loop_for():
    itens = [1, 2, 3, 4]
    for item in itens: 
        print(item)

def loop_for_2():

    for a in range(15):
        print(a)

def loop_for_3():

    itens = [1, 10, 20, 30, 40]
    for index, item in enumerate(itens): # retorna uma lista de tuplas (indice, item)
        print("Indice: ", index)
        print("Item: ", item) 


def loop_for_4():

    # break e continue

    itens = ["Lucas", "Marcos", "Mateus"]
    for item in itens:
        if item == 'Marcos':
            print("Marcos encontrado...")
            continue # evita a execução atual do bloco  

        print(item) 

def loop_for_5():

    # break e continue

    itens = ["Lucas", "Marcos", "Mateus"]
    for item in itens:
        if item == 'Marcos':
            print("Marcos encontrado...")
            break # Para a execução do loop assim   

        print(item) 

def main():
    # loop_for()
    # loop_for_2()
    loop_for_4()


if __name__ == '__main__':
    main()