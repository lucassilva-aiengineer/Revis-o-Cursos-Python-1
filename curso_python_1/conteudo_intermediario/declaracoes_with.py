# With 

# Lidando com arquivos por meio de exceções 


nome_arquivo = "arquivos_dados\\texto_teste.txt"


def utilizando_try_ex():
    try:
        arquivo =  open(nome_arquivo, "r") # Método de leitura 
        content = arquivo.read()
        print(content)


    finally:
        print("Fechando arquivo!")
        arquivo.close()

def utilizando_with():

    # Abrindo arquivo, fechando automaticamente. 
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

def main():

    utilizando_with()

if __name__ == '__main__':
    main()
