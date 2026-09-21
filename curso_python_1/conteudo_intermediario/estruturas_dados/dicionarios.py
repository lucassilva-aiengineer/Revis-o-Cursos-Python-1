# Dicionários 
# Estruturas de dados ordenadas, organizada em pares de chave-valor onde pode-se acessar elementos por meio destas. As listas 
# podem recepcionar quais quer tipos de estruturas de dados e dados, como listas, tuplas, conjuntos/outros dicionários. 


def dicionarios_parte_1():
    pessoas_1 = {
        "nome": "Lucas",
        "idade": 10,
        "altura": 110
    }


    print(pessoas_1["nome"])

    # Acessando elementos com o método get() 
    # Podemos imprimir valores padrão caso a chave não seja encontrada. 
    print(pessoas_1.get("altura", "altura não encontrada"))

    # Removendo chaves de um dicionário 

    try:
        print(pessoas_1.pop("chave"))

    except KeyError as message:
        print(f"""Chave não encontrada
Código do Erro (Chave que causou o erro): {message}""")

    # Removendo a último par chave valor que foi inserido no dicionário 
    print(pessoas_1.popitem())

    # Verificando uma chave num dicionário 

    print("nome" in pessoas_1)


    # Uma lista com todas as chaves de um dicionário 

    print(pessoas_1.keys())

    # Lista de dicionários
    print(list(pessoas_1.keys()))


    print(pessoas_1.values())
    print(list(pessoas_1.values()))

    # Uma lista com os itens do dicionário, 
    # representados em uma tupla onde o primeiro índice da tupla é a chave e o segundo o valor associado. 

    print(list(pessoas_1.items()))

    # Contando a quantidade de itens que fazem parte 

    print(len(pessoas_1))

def dicionarios_parte_2():

    def parte_a():
        pessoas = {
            "pessoa_1": "Marcos",
            "pessoa_2": "José"
        }

        # adicionando elemento 
        pessoas["pessoa_3"] = "João"
        pessoas["pessoa_4"] = {
            "nome": "Lucas",
            "idade": 21 
        }

        print(pessoas)

        # Removendo elementos do dicionário 

        try:
            del pessoas["pessoa_1"]

        except Exception as message: 
            print("Pessoa não encontrada!")

        else: 
            print("Nenhum erro encontrado!")

        
        finally:
            print("Código executado com sucesso.")

        
        try:
            del pessoas["pessoa_1"]

        except Exception as message: 
            print("Pessoa não encontrada!")

        else: 
            print("Nenhum erro encontrado!")

        
        finally:
            print("Código executado com sucesso.")


    
    def parte_b():

        """
            Dividindo a função em duas partes 
            a fim de otimizar a saída. 
        """ 

        dicionario = {
            "chave_1": "a", 
            "chave_2": "b",
            "chave_3": "c"
        }


        print(dicionario["chave_1"])

        # Criando uma cópia do dicionário 

        copia_dicionario = dicionario.copy()

        print(copia_dicionario)

def main():

    # dicionarios_parte_1()

    dicionarios_parte_2()




if __name__ == '__main__':
    main()