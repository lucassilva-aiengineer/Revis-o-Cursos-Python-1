def argumentos_posicionais(a, b, c):
    print(a, b, c)



# Args e Kwargs.
# Uma forma de termos uma quantidade indeterminada de argumentos de palavra chave, 
# e uma quantidade indeterminada de argumentos posicionais 

def args_kwargs(a, b, *args, **kwargs):

    print(a, b)

    print("Argumentos Posicionais: \n")
    for arg in args:
        print(a)

    print("Argumentos de palavra chave: \n")
    for chave in kwargs:
        print(chave)

    print(int(kwargs['j']) * 10)

def teste_1():

    argumentos_posicionais(10, 20, 30)
    argumentos_posicionais(c= 30, b= 20, a= 10)
    argumentos_posicionais(a= 30, b= 10, c= 20)



def teste_2():

    args_kwargs("a", "b", "c", "d", "e", "f", g= "1", h= "2", i= "3", j= "4")



def main():
    
    teste_2()



if __name__ == '__main__':
    main()