import random


# Recursividade 
# Uma função que chama a si mesma até que uma condição seja cumprida. 


def exemplo_1():

    def buscar_nomes(lista: list, nome: str, tentativas= 1)-> None:

        """
            Exemplo de função recursiva.
        """

        indice = random.randint(0, len(lista) - 1)
        if lista[indice].lower() != nome:
            tentativas += 1
            buscar_nomes(lista, nome, tentativas)

        else:
            print("Elemento encontrado!")
            print("N° Tentativas {}".format(tentativas))


    nomes = ["marcos", "João", "José"]
    buscar_nomes(nomes, "marcos")

    def factorial(n):

        # Fatorial de 10 = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
        if n == 1: return 1
        return n * factorial(n - 1)

    print("O fatorial de 10: {}".format(factorial(10)))
def main():
    

    exemplo_1()


if __name__ == '__main__':
    main()