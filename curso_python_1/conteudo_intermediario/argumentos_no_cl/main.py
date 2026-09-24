# Aceitando argumentos em linha de comando  CL

import sys 
import time

def aprensentando():
    print("Argumentos impressos: " + str(sys.argv))

    nome = sys.argv[1] if len(sys.argv) >= 1 else None 


    print(f"Olá o meu nome é {nome if isinstance(nome, str) else str(nome)}")



# aprensentando()

# Utilizando outra bíblioteca 

import argparse
def outra_biblioteca():

    parser = argparse.ArgumentParser(
        description= "Este algoritmo realiza uma multiplicação."
    )

    # Definindo o argumento, setando o argumento. 

    parser.add_argument('-f', '--fator', metavar= 'fator',
    required= True, help= 'O fator da múltiplicação.',
    choices= {"fator_a", "fator_b"} # Opções que podem ser selecionadas
    )

    args = parser.parse_args()

    try:    
        print(args)
        # print(f"{args.fator} * 10 = {int(args.fator) * 10}")
        # print(args)
        # print(type(args))

    except TypeError as message:
        print("{}".format(message))
        print("Tentando novamente...")
        time.sleep(0.2)

    else:
        print("Nenhum erro encontrado!")

    finally:
        print("Código executado com sucesso...")



def main():

    outra_biblioteca()



if __name__ == '__main__':
    main()