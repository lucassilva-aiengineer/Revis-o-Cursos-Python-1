import time 


def ola(nome):
    print(f"Olá {nome}!")
    """
        As funções sã blocos de código reutilizáveis, ativados somente quando chamados
    """



def saudacoes():

    """
        Parâmetros, argumentos, um argumento é algo como uma variável/informação mutável e que muda os cálculos, tipo x em f(x) = 2x + 10
        que podem ser utilizados no interior da função, conforme o argumento muda o resultado da função muda. -> Entrada -> Código -> Saída 
    """


# É como assistir a um filme 

def saudacao_especifica(nome, sobre_nome, idade= 21, user= "user1"):

    print(f"Olá user! {user}:")
    print(f"...")
    time.sleep(0.2)
    print(f"""Meu é {nome} {sobre_nome} e tenho {idade} anos """)


# Escopo de variável 
# São o nível de acesso que nós temos de certa variável.


def escopo(valor: int):

    valor = 10

def testando_1(estrutra_mutavel, chave: str):

    estrutra_mutavel[chave] = "novo_nome"


def run():

    # Um tipo de dados imutável
    # valor = 5
    # escopo(valor)


    # print(valor)

    dicionario = {
                    "nome": "Mateus", 
                    "idade": 21
                
                    }


    # As estruturas de dados
    testando_1(dicionario, "nome")

    print(dicionario)


def saudacoes_2(name= ""):

    # if not name:
    #     return # A função deixará de ser executada 
    # print("Olá" + name + " !") 

    return "Olá! " + name + " !"


def escopo_variavel():

    # Não de modificação, mas alcance.
    idade = 10 # Declarado no escopo global acesso em todos os outros, incluindo local nas funções.


    def teste():

        escopo_local = "Lucas" # A variável de escopo local não pode ser acessado
        
        print("Acessando a variável na função: ", idade)

    teste()
    print(idade)

    
    print(escopo_local)


def funcoes_aninhadas():

    # Funções codificadas no interior de outras funções 

    # def conversa(frase):
    #     def dizer(palavra):
    #         print(palavra)

    #     palavras = frase.split(' ')
    #     for palavra in palavras: 
    #         conversa(palavra)

    def dizer(palavra):
        time.sleep(0.2)

        if palavra.startswith("E"):
            print("\n\n")
        print(palavra.upper())

    def conversa(frase):
        # Quebro a frase em uma lista de palavras
        
        palavras = frase.split(' ')
        for palavra in palavras:

            # Funções aninhadas na aplicação, que é no caso a mesma coisa que a função 
            # tivesse sido definida no interior da função. 

            dizer(palavra)

    
    conversa("Eu sou um campeão, eu confio no Senhor Deus!")


def exemplo():

    def count():
        count = 0

        def increment():
            nonlocal count # Assim posso acessar a variável fora desta função 
            count = count + 1
            # count += 1

            print(count)
        
    
        increment()

    count()


# Clousers 
# Uma forma de criar uma memória persistente? 

def teste():

    def counter():
        count = 0 

        def increment():
            nonlocal count 
            count = count + 1
            return count 

        return increment 


    increment = counter()  

    
    print(increment())
    print(increment())
    print(increment())
    print(increment())


def main():

    # ola()  

    # saudacao_especifica("Lucas", "Soares da Silva")

    # run()

    # print(saudacoes_2("Marcos"))

    # escopo_variavel()
    # funcoes_aninhadas()
    # count()
    # exemplo()

    teste()
    


if __name__ == "__main__":
    main() 
