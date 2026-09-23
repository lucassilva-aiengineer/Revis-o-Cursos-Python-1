import time
def falar():

    for a in range(5):
        for n in range(10):
            time.sleep(0.2)
            string = n * "\t"
            print(string +" Falando...")

    # ... 

def main():
    print("Testando funções...")
    falar()


# Só executa o arquivo quando estamos utilizando diretamentem, não pela importação. 
if __name__ == '__main__':
    main()
