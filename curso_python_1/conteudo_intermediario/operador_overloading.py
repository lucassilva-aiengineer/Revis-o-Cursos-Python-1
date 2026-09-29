# Operador Overloadin


class Pessoa:

    def __init__(self, nome, idade):

        self.nome = nome 
        self.idade = idade 


    # Método mágico 
    def __gt__(self, outro):
        return True if self.idade > outro.idade else False # Comparando dois objetos por meio deste método mágico 


p1 = Pessoa("Marcos", 10)
p2 = Pessoa("Lucas", 12)

print(p1 > p2)