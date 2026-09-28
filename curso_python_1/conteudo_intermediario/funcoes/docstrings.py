
# Docstrings 
# Docstrings são formas de registrar informações sobre o seu código, tanto a si como a outros colegas. 


""" 
    Docstrings de arquivo 
    Este é o arquivo que fala sobre sobre docstrings 
    docstrings de muitas linhas 

"""

class Pessoa:

    """
        Docstrings de classe
    """

    def __init__(self, nome, idade):
        
        """
            Docstrings de método 
            Método construtor
        """
        
        self.__nome = nome 
        self.__idade = idade




def main():

    help(__name__)
    help(__name__.Pessoa)
    help(Pessoa)


if __name__ == '__main__':
    main()