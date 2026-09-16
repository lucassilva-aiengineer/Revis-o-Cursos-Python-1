# Tuplas 


# Tuplas são estruturas de dados ordenadas, que permitem duplicação de elementos, porém não permitem modificação. 


def tuplas():
    nomes = ("Marcos", "João", "Lucas")

    # Acessando elementos pelos índices 
    print(nomes[-1])
    print(nomes.index("Marcos"))

    print(len(nomes))


    # Uma lista de elementos de uma tupla

    print("Lucas" in nomes)


    print(sorted(nomes))

    # Criando duas tuplas por meio de uma
    nova_tupla = nomes + ("nome_1", "nome_2")


def main():

    tuplas()



if __name__ == '__main__':
    main()