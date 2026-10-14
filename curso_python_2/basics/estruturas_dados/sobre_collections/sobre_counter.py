# A bíblioteca collections se trata de um módulo dedicado a lidar com estruturas 
# de dados, tanto na manipulação destas, como oferecendo estruturas de dados especiais.  

from collections import Counter 

# Counter 


def funcao():

    letras_a = "aaaaaaaaabbbbbbbbbbccc"
    contador = Counter(letras_a)

    print(contador)

    # O objeto Counter() retorna em formato de dicionário as quantidades de vezes que os elementos aparecem 
    # em uma estrutura de dados.

    print(contador.items())

    print(f"Chaves em contador: {contador.keys()}\n")
    print("Valores em contador: {}".format(contador.values()))
    print(f"\n Elementos mais comuns no contagem: {contador.most_common(1)[0][0]}")

    print(list(contador.elements()))
def main():

    funcao()


if __name__ == '__main__':
    main()