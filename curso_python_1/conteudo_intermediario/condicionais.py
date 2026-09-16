

def condicionais():

    """
        Estruras que executam blocos de código, caso uma 
    """

    nome = "Marcos"

    if nome.lower() == "marcos":
        print("Hello Marcos!")

    elif nome.lower() == "Lucas":
        print("Hello Lucas!")

    elif nome.lower() == "João":
        print("Hello João!")

    else:
        print("Este nome não consta nos registros de nomes !")


def main():
    condicionais()



if __name__ == "__main__":
    main()