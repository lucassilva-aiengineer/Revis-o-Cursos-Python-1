# Exceções 


# Nós tentamos executar um bloco de código 
# caso identifiquemos um erro de Exceção 

import time


def try_except():

    try:
        # Algumas linhas de código 

        n_a = int(input("Indique a divisão a: "))
        n_b = int(input("Indique a divisão b: "))

        resultado = n_a / n_b 
        print("Resultado: ", resultado)

    except ZeroDivisionError as message:
        print(message)

        print("A divisão por zero não é matemáticamente possível!")
        print("Tentando novamente...")
        time.sleep(3)

        try_except()



    except TypeError as message:
        print(message)


    else:
        print("Nenhum erro foi encontrado!")


    finally:
        print("Código finalizado, independente de erros encontrados ou não.")



def raise_exception():

    try:
        
        a = 10 
        b = 5 

        if b == 0:        
            raise Exception("An error!")

        resultado = a / b
        print(f"Resultado: {resultado}")


    except Exception as message:
        print(message)


# Criando as nossas próprias classes de exceção 

def classe_excessao(): 

    # A nossa própria classe de exceção 
    class PeopleNotException(Exception):

        print("Indiside")
        pass 


    try:
        raise PeopleNotException()

        # Com as exceções podemos criar alternativas para o  código perante 
        # os erros de exceção.


    except PeopleNotException:
        print("Pessoa não encontrado!")



    
    

def main():

    # try_except()

    # raise_exception()
    classe_excessao()


if __name__ == '__main__':
    main()