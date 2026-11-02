import random

# Biblioteca random

# Números decimais entre 1 e 10, incluindo o e o 10 
a = random.uniform(1, 10)
print(a)


# Um número inteiro entre 1 e 10, incluindo o 1 e o 10 
b = random.randint(1, 10)


# Um número inteiro entre 1 e 10, não incluso o 10. 

c = random.randint(1, 10)
print(b)


# Uma distribuição normal (Poisson)
d = random.normalvariate(0, 1) 
print(d)


# Minha lista
lista_letras= list("ABCDEFG")
letra = random.choice(lista_letras)
print(letra)

# Uma fração da lista original
parte_lista = random.sample(lista_letras, 2)
print(parte_lista)

letras = random.choices(lista_letras, k= 3)
print(letras)


# Embaralhando uma lista

random.shuffle(letras)
print(letras)


def teste_random()-> None:
    # Mantendo os valores 
    import random 

    print("Testes 1")
    print(random.random())

    random.seed(1)
    print(random.randint(0, 10))


    random.seed(1)
    print(random.randint(0, 10))

    random.seed(1)
    print(random.randint(0, 10))



def teste_secrets():

    import secrets 

    # Uma biblioteca mais segura que a biblioteca random 

    print("Testes 2")
    print("Lib Secrets")

    numero_aleatorio = secrets.randbelow(10)
    print(numero_aleatorio) # Um número aleatório inferior a 10.  

    numero_binario_aleatorio = secrets.randbits(5) # Um número que utiliza até 5 algarismos na representação binária 11111
    print(numero_binario_aleatorio)


    minha_lista = list("ABCDEGHIJK")
    
    elemento_a = secrets.choice(minha_lista)

    print(elemento_a)


def teste_numpy():

    def parte_1():
        try:
            import numpy as np

        except ModuleNotFoundError as message:
            print(message)
            print("Módulo Não Encontrado!")


        print("Testes 3")
        print("Lib Numpy")

        print(np.__version__)

        numero = np.random.randint(0, 100)
        print(numero)

        vetor = np.random.randint(0, 10, 10)
        print(vetor) 

        Matriz_a = np.random.randint(0, 100, (2, 5))
        print(Matriz_a)

        # Embaralhando um vetor 

        Matriz = np.array([
                            [1, 2, 3], 
                            [4, 5, 6],
                            [8, 9, 10]
        ]) 
        print(Matriz)

        np.random.shuffle(Matriz)

        print(Matriz)


        np.random.seed(1)   
        print(np.random.rand(3, 3))

        np.random.seed(1)
        print(np.random.rand(3, 3))


    parte_1()

def main():

    # print("Testes 1:")
    # teste_random() 

    # teste_secrets()

    teste_numpy()



if __name__ == '__main__':
    main()
