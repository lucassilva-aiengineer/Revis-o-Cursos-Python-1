# Strings 


def strings():
    minha_string_1 = "Olá mundo!"

    # Aspas no interior das strings 

    minha_string_2 = "'Por que o viver é Cristo e o morrer é lucro' - Paulo de Tarsso"
    print(minha_string_2)


    minha_string_3 = """
        Uma string de muitas linhas 
    """

    print(minha_string_3)


def strings_1():

    # Acessando caracteres de uma string 

    minha_string = "Hello World"
    print(minha_string[0]) 

    # Fatiando uma string 
    print(minha_string[:6])

    # Imprimindo um a cada dois caracteres
    # Indo do primeiro ao último caracter
    print(minha_string[:-1:2])

    # Revertendo uma string 
    string_a = "Hello World"

    print("========= Revertendo A String =========")
    print(string_a[::-1])

def strings_2():

    saudacao = "Olá usuário"
    nome = "Lucas"
    frase = saudacao + " " + nome
    print("Frase: " + frase + "!") 

    # Iterando sobre os caractes 

    for letra in frase:
        print(letra)

    letra = "a"
    if letra in frase:
        print(f"Sim a letra: {letra}")

    else:
        print("A letra", letra, "não está na string.")
    

def strings_3(): 
    """
        Uma função com vários métdos strings 

    """
    nome = "    Lucas Soares da Silva     "
    print("Nome não tratado{}".format(nome))
    print("Nome", nome.strip())

    print(nome.upper())
    print(nome.lower())

    nome = nome.strip()

    print(nome.startswith('L'))
    print(nome.endswith("s"))


    print(nome.find("ca"))

    print(nome.count("a"))


    # Substituindo paretes da nossa string
    print(nome.replace("Silva", "SILVA"))

    # Transformando
    # Uma string em uma lista de caracteres  
    nome = "L,u,c,a,s,S,o,a,r,e,s"

    lista_string = nome.split(",")
    print(lista_string)

    # Juntando a lista em uma string por meio de uma separador
    minha_string = " ".join(lista_string)
    print(minha_string)


def string_4():

    def formato_antigo():
        # Formatação de string 
        nome = "Lucas"
        idade = 12.5
        frase = "O meu nome é %s" % nome # Bem com a linguagem
        frase_com_numero = "O meu nome é Lucas e a minha idade é %d anos" % idade
        frase_com_decimal = "O meu nome é Lucas e a minha idade é %f anos" % idade

        # print(frase)
        # print(frase_com_numero)
        print(frase_com_decimal)

    def formato_2():
        idade = 21.954030

        frase = "A minha idade é {:.2f} a idade dos meus amigos é {}".format(idade, idade)
        print(frase)


    def formato_3():

        idade = 21.954030

        frase = f"A minha idade é {idade:.2f} a idade dos meus amigos é {idade}"
        print(frase)

        
    # formato_2()
    formato_3()

def outras_coisas()-> None:
    from timeit import default_timer as timer 
    
    minha_lista_1 = ["a"] * 10
    print(minha_lista_1)

    start_1 = timer()
    string = ""
    for i in minha_lista_1:
        string += i

    stop_1 = timer()
    
    print("Juntando os itens da lista: " + string)

    start_2 = timer()
    print("\nUtilizando o método Join: " + ",".join(minha_lista_1))
    stop_2 = timer()

    print("Tempo 1: {}".format(stop_1 - start_1))
    print("Tempo 2: {}".format(stop_2 - start_1))


def main():
    # strings()
    # strings_1()
    # strings_3()
    # outras_coisas()

    string_4()


if __name__ == '__main__':
    main()