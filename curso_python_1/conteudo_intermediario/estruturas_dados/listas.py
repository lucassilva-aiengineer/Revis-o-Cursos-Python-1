
def listas():

    """
        Listas são estruturas de dados, ordenadas, indexadas e que aceitam elementos duplicados, 
        de um ou vários tipos de dados, diferente da linguagem c.  
    """

    nomes = ["Marcos", "Mateus", "João", "José", "Lucas"]

    print("Marcos" in nomes)


    # Acessando os elementos pelos índices. 

    print(nomes[0])

    # Alterando valores 

    nomes[-1] = "José"

    print(nomes)

    print("Antes da alteração: " + str(len(nomes)))

    # Adicionando elementos 
    nomes.append("Jonas")

    print("Depois da alteração:", len(nomes))

    # Juntando listas 

    nomes.extend(["Jonas", "Moisés", "Davi", "Samuel"])
    
    print("Depois de extendemos a lista: " + str(len(nomes)))

    nomes += ["Nome 1", "Nome 2"] 

    nomes += "NOME 3"

    # Removendo

    nomes.remove("Nome 2")

    # Removendo o último item da lista 

    nome_removido = nomes.pop() 

    print(f"Item removido: {nome_removido}")

    # Adicionando dados a um índice específico 

    nomes.insert(2, "nome_teste")

    print("Nomes:", nomes)

    # Incluindo uma sequência de itens numa sequência de itens

    nomes[2:5] = ["Teste 1", "Teste 2"]
    # print(nomes)

    print(nomes)

def listas_1():

    lista = ["Marcos", "João", "Otávio", "Mateus", "Lucas", "José", "Luiz", "Carlos", "Enoque", "marcos", "jose", "bruno", "julio"]

    # lista.sort() # Ordena as minúsculas por último 

    lista.sort(key= str.lower) # Altera a lista original 

    # Cópia 

    lista_copia = lista[:]

    lista_copia.sort()

    print("Lista Original: ", lista)
    print("Lista Cópia: ")

    print(lista)


    # Ordenando elementos sem alterar a lista original 

    elementos = sorted(lista, key= str.lower)

    print(sorted(lista, key= str.lower))

    print(elementos)

def main():
    # listas()
    listas_1()

if __name__ == '__main__':
    main()