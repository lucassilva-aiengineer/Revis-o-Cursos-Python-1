import random 
from faker import Faker
from typing import List

# Um jogo de chutar nomes 


def selecionar_nomes()-> List[Faker]:
    """
        Essa função seleciona e retorna 10 nomes aleatórios  
    """
    faker = Faker('pt-BR')

    return [faker.name() for a in range(10)]


def mostrar_nomes(lista_nomes: List[Faker])-> None:

    """
        Função que Exibe os Nomes.
    """

    n = 0
    for nome in lista_nomes:
        print(f"nome n° {n + 1}: {nome}")
        n += 1

def acertar_nomes(lista_nomes, resposta)-> bool:

    """
    A parte que seleciona o nome aleatóriamente e 
    recebe a resposta.
    """
    random.shuffle(lista_nomes)
    nome_selecionado = random.choice(lista_nomes).lower()

    if nome_selecionado == resposta.lower():
        return True 

    else:
        return False


# def run(lista_nomes)-> bool:

#     score = False

#     # Exibe os nomes
#     mostrar_nomes(lista_nomes)
#     # Colhe a resposta 
#     resposta = input("Indique a sua resposta: ")

#     if acertar_nomes(lista_nomes, resposta):
#         score = True

#     else:
        
#         print("Deseja tentar novamente (s/n)?")
#         resposta = input("Indique a sua resposta: ")

#         if resposta.lower() == "s":
#             run(lista_nomes)

#         else:
#             print("Encerrando rodada!")
#             return score




def main():

    while True: 

        print("""
============ Menu ============
    - 1 Para Uma nova rodada do jogo""") 
    # Pausando o desafio por hora
    # print(acertar_nomes(["Marcos"], "Marcos"))




if __name__ == '__main__':
    main()

