

# Números absolutos (Módulo de um número) 

valor = -5 

import numpy as np


def valores_absolutos():
    print("O  valor absoluto de -5 é {}".format(abs(valor)))


    rng = np.random.default_rng()

    vetor_inteiros = rng.integers(low= -100, high= -1, size= 10)

    valores_absolutos = np.array([abs(valor) for valor in vetor_inteiros])
    for valor in valores_absolutos:
        print(valor)


def arredondando_valores():

    """
        Uma função que arredonda o valor decimal, floats, para o valor inteiro
        mais próximo. 
    """

    print(round(10.5))
    print(round(10.52))


    # Podemos ajustar a precisão decímal. 

    print(round(10.53, 1))


def main():

    arredondando_valores()


if __name__ == '__main__':
    main()

