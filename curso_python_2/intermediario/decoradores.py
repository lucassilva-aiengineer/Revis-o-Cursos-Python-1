# Decoradores 
import time 

def decoradores_sem_argumentos():

    def start_end_decorator(funcao):

        def wrapper():

            print("Executando algo antes da função...")
            time.sleep(1.5)
            funcao()
            print("Executando algo após da função...")


        return wrapper


    @start_end_decorator
    def print_nome():
        print("Lucas")


    # print_nome = start_end_decorator(print_nome)


    print_nome()

# Decorador: uma função que executa 
# uma função como argumento, por isso "altera" o comportamento da função agregando novos comportamentos. 
 
def decoradores_com_argumentos():

    def meu_decorador(funcao):

        # *args, quantidade indeterminada de argumetos posicionais. 
        # **kwargs, argumentos de palavras, nomeados. argumento_1 = 10

        def wrapper(*args, **kwargs):

            print("Contagem...")
            
            for a in range(10):
                print(a)
                time.sleep(0.1)

            funcao(*args, **kwargs)

            print("Função concluída...")
            time.sleep(1)

        return wrapper 


    @meu_decorador
    def print_nome(nome):
        print(f"Olá {nome}")

    # print_nome = meu_decorador(print_nome)
    # print_nome("Marcos")


    print_nome("Marcos...")


# def decoradores_parte_3():

#     import functools 

#     def repeat(funcao):
#         def wrapper(numero: int):
#             for n in range(numero):
#                 funcao()

def decoradores_parte_3():
    import functools 

    def repeat(num_times):
        def decorator_repeat(funcao):
            @functools.wraps(funcao)
            def wrapper(*args, **kwargs):
                for n in range(num_times):
                    print("Excutando a função: n°", n + 1)
                    result = funcao(*args, **kwargs)
                return result 
            return wrapper  
        return decorator_repeat 

    @repeat(num_times= 2)
    def great(nome):
        print(f"Hello {nome}!")

    great("Lucas")

def main():
    # decoradores_com_argumentos()
    decoradores_parte_3()

if __name__ == '__main__':
    main()