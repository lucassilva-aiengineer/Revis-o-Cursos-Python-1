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

def run():

    valor = 5
    escopo(valor)

    print(valor)


def main():

    # ola()

    # saudacao_especifica("Lucas", "Soares da Silva")

    run()



if __name__ == "__main__":
    main() 
