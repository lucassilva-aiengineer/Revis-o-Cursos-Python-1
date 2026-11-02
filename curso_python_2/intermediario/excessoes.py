# Exceções 

# Criando nossas exceções 

def excessoes_raise():

    # numero = int(input("Indique um número inteiro positivo: ")) 

    numero_b = 9
    if numero_b < 10:
        raise Exception('O numero deve ser necessáriamente maior que dez')

    
    # numero_b = 10 

    # Uma verificação, caso verdadeira, prosseguimos com a execução do código 
    # caso contrário teremos um erro. 

    assert (numero_b > 11), "O número deve ser maior que 11!" 


def blocos_try_except():

    def forma_1():
        try:
            a = 5 / 0 

        except:
            print("Temos um erro de exceção não identificado!")


    def forma_2():

        try:
            a = 10 
            resultado = a / 0 

        except ZeroDivisionError as message:

            print("Message: ", message)

        else:
            print("Nenhum erro de exceção ocorreu!")

        finally:
            print("Código finalmente executado!")


def nossas_classe_de_excessao():
    
    class ValorMuitoAlto(Exception):
        pass 


    class ValorMuitoBaixo(Exception):

        def __init__(self, messagem, valor):
            self.message = message
            self.valor = valor 


        


    def testar_valor(n):

        if n > 10:
            raise ValorMuitoAlto("Valor Muito Alto!")
        

        if n < 10:
            raise ValorMuitoBaixo("Valor Muito Baixo!", n)



    try:
        testar_valor(10)
        
    except ValorMuitoAlto as message:
        print(message)

    except ValorMuitoBaixo as objeto_erro:
        print(objeto_erro.message)
        print(objeto_erro.valor)

    else:
        print("Erros não encontrados!")


            
def main():
    
    # excessoes_raise()
    nossas_classe_de_excessao()




if __name__ == '__main__':
    main()