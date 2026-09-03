
def condicionais()-> None:

    idade = 40 
    if idade >= 18:
        print("Maior que dezoito anos!")

    else:
        print("Menor que dozoito anos!")


def operador_ternario()-> bool:

    """
        Uma forma mais simples de elaborar uma estrutura de condicional. 
    """

    idade = 10
    return True if idade > 18 else False 

def main():

    # condicionais()

    operador_ternario()

if __name__ == '__main__':
    main()