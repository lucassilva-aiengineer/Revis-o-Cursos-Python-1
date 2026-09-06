
# Tipos de Dados Numéricos 




# Números Imaginários:

def imaginarios():

    """
        Trabalhando com dados imaginários 
    """
    num_1 = 2 + 3j

    # Parte real e parte imaginária 

    print(num_1.imag)
    print(num_1.real)


    num_2 = complex(2, 3)

    print(f"""Parte real: {num_2.real}
Parte Imaginária: {num_2.imag}""")




def main():

    imaginarios()

if __name__ == '__main__':
    main()