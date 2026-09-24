# Funções lambda 

# Funções anônimas

# palavra_chave arg_a, arg_b : expressao 
# lambda a, b: a * b


# São funções muito utilizadas com argumento de funções maiores. 


def intr():
    lambda num : num * 10

    mult = lambda a, b : a * b

    print(mult(10, 2))



# map(), filter(), reduce()

# map()
# A função map() percorre um iterável, como lista, aplicando uma função, utilizando os itens como argumento. 

def funcao_map():
    lista = [1, 2, 3]

    def double(a):
        return a * 2

    # resultado = map(double, lista)

    resultado = map(lambda a : a * 2, lista)
    print(lista)
    print(list(resultado))

def main():
    # intr()
    funcao_map()



if __name__ == '__main__':
    main()