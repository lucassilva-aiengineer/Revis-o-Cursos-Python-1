

def strings():

    # "Nome"

    """
        Uma cadeia de caracteres 
    """
    nome = 'Marcos'

    # Concateação
    frase = "Meu nome é " + nome + " ." 

    print(frase)

    # Encrementando uma string 

    nome_a = "Marcos"

    nome_a += " Silva"

    print(nome_a)   

    nome_a += " Eu tenho "
    nome_a += str(39) 

    nome_a += " anos de idade."

    print(nome_a)

    print("""

        Meu nome é Lucas 
        Possuo 21 anos.
        E esta é uma string de muitas 
        linhas. 
    """)


def metodos_string()-> None:

    nome = "Lucas"
    print(nome.upper())

    print("Letra minúsculas".lower())

    print("lucas silva".title())

    print("lucas silva".capitalize())

    print("letras minusculas".islower())


    print("AS LETRAS SAO MAIUSCULAS".isupper())


    print("Inicia com a letra I".startswith("I"))

    print("Finaliza com a letra A".endswith("A"))

    print("trocar a letra a pela letra a".replace("a", "j"))

    minha_string = "Eu, tenho, 21, anos"

    minha_lista = minha_string.split(",")

    print(minha_lista)

    print("".join(minha_lista)) # Transformando uma lista novamente em uma string.

    # Encontrando o índice inícial de uma substring. 

    print("minha string".find("m"))

    print(len(minha_string))

    print("Eu" in minha_string)


def escape_sequence():

    nome = "Mar\"cos"

    nome_a = 'Mar"cos'

    new_line = "Mat\neus"

    print(new_line)

    exemplo = "Mat\\eus"

    print(exemplo)


def fatiamento_strings()-> None:

    """
        Fatiamento de strings/ assessando caracteres pelo índice.
    """
    texto = "Lucas gosta de chocolate"

    print(texto[0])

    print(texto[0: 2])

    print(texto[:5])

    print(texto[2:])

    print(texto[-1])

    print(texto[-2])

    print(len(texto))

    print(texto[0: 8: 2])

    print(texto[:: -1]) # Acessa as letra voltando. 


def main():

    # strings()

    # metodos_string()

    # print("")

    # escape_sequence()

    fatiamento_strings()

if __name__ == '__main__':
    main()