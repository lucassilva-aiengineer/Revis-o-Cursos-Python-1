# Classes 


# Nós criamos classes, algo que é como a planta de uma casa, a arquitetura de um objeto. 
# E apartir disto criamos as casas, as instâncias daquela arquitetura, nós seguimos aquele 
# desing. 

class Pessoa:
    def falar(self): # Cada objeto 
        print("Pessoa falando...")



# Construtores e atributos 

class ObejetoPessoa1:
    def __init__(self, idade, nome):

        self.nome = nome # Recebemos parâmetros na criação do objeto e associamos este parâmetros ao objeto criado como atributo. 
        self.idade = idade

    
    def falar(self): # Cada objeto 
        print("Pessoa falando...")

# p1 = Pessoa()
# p1.falar()


# Herança 
# Um forma de fazer com que as classe filhas herdem atributos e métodos da classe mãe 

class Funcionario(ObejetoPessoa1):

    # def __init__(self, salario):
    #     # __init__.super()

        ... 
    
def main():

    p1 = ObejetoPessoa1(10, "Marcos")

    print(p1.idade)
    p1.falar()

    f1 = Funcionario(10, "Lucas")
    f1.falar()


if __name__ == '__main__':
    main()

