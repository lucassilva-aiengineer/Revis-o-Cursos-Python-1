class Cliente:

    def andar(self):
        print("Andar...")


class Funcionario:

    def andar(self):
        print("Andar...")



p1 = Cliente()
p2 = Funcionario()

# Temos métodos iguais em classes diferentes 
# deste modo não precisariamos de duas classes uma única classe serviria muito bem para 
# representar os mesmos objetos. 

p1.andar()
p2.andar()
