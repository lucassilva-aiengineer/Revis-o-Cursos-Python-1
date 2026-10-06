# Dicionários 


def dicionario_p1():
    meu_dicionario = {
        "nome": "Mateus",
        "Idade": 21,
        "Cidade": "New York"
    }

    print(meu_dicionario)

    meu_dicionario_2 = dict(nome= "Lucas", idade= "21", cidade= "Boston")
    print(meu_dicionario_2)


    # Acessando valores por meio da chave

    valor = meu_dicionario["nome"]
    print(valor)


    # Dicionários são mutéveis, não permitem duplicatas, temos conjuntos chave valor. 

    meu_dicionario["email"] = "mateus@gmail.com"

    print(meu_dicionario["email"])

    meu_dicionario["email"] = "mateus1@gmail.com"
    print(f"{meu_dicionario["email"]}")

    # Deletando chaves 

    del meu_dicionario["nome"]
    print(meu_dicionario["nome"]) if "nome" in meu_dicionario else print(None)


    # Removendo uma chave 

    meu_dicionario.pop("idade", "Idade não encontrada!")

    print(dicionario_p1["idade"]  if "idade" in meu_dicionario else False)

    print(meu_dicionario.keys())

    meu_dicionario.popitem()

    print(meu_dicionario.get("email", "Chave não encontrada!"))


def dicionario_p2():
    
    dicionario = {
        "nome": "Marcos",
        "idade": 10
    }

    if "nome" in dicionario:
        print(dicionario["nome"])

    else:
        print("Chave não encontrada!")


    try:
        print(dicionario["ultimonome"])

    except KeyError:
        print("Error")


def dicionario_p3():

    dicionario = {
        "nome": "Marcos",
        "idade": 10,
        "email": "marcos@gmail.com"
    }


    print("Chaves: ")
    for key in dicionario.keys():
        print(key)


    print("\nValores: ")
    for value in dicionario.values():
        print(value)


    print("\nChave Valor: ")   
    for chave, valor in dicionario.items():
        print(f"""Chave: {chave}
Valor: {valor}\n""")



def dicionario_4():

    dicionario = {
        "nome": "Marcos",
        "idade": 10,
        "email": "marcos@gmail.com"
    }

    # Copiando um dicionário

    copia_fake = dicionario
    copia_dicionario = dicionario.copy()
    copia_2 = dict(dicionario)

    copia_fake["telefone"] = "(00) 00000 - 0000"
    
    copia_dicionario["email"] = "marcos@gmail.com"
    copia_2["endereco"] = "rua123 Rio de Janeiro RJ"

    print("Dicionário Original: ")
    print(dicionario)
 
    print("\nCopia Fake:  ")
    print(copia_fake)

    print("\nCopia Real 1")
    print(copia_dicionario)

    print("\nCopia Real 2")
    print(copia_2)



def dicionario_5():

    meu_dicionario = {"nome": "Marcos", "idade": 20, "email": "marcos@gmail.com"}
    meu_dicionario_2 = dict(nome= "Mateus", idade= 30, cidade= "Goiânia")

    meu_dicionario.update(meu_dicionario_2) # O segundo dicionário é atualizado para ter as mesmas chaves que o primeiro tem

    print(meu_dicionario)


    # Nós podemos ter chaves imutáveis. 

    dicionario = {3: 9, 6:36, 9:81}
    print(dicionario)

    elemento = dicionario[0]
    print(elemento)


    minha_tupla = (8, 7) # 

    dicionario_4 = {minha_tupla: 10}
    print(dicionario_4)
    
def main():
    # dicionario_p1()
    # dicionario_p2()
    # dicionario_p3()
    # dicionario_4()

    dicionario_5()


if __name__ == '__main__':
    main()