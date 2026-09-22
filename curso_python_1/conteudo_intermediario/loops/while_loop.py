
def loop1():

    condicao = True 
    while condicao == True:

        print("A condição é verdadeira!")
        condicao = False 


def loop2():
    # Condição de parada, 
    # implícita.

    count = 0 

    while count < 10:
        print("A condição é verdadeira!")
        print(f"Contagem: {count + 1}")
        count += 1 


    print("Depois do loop")

def main():

    # loop1()
    loop2()

if __name__ == '__main__':
    main()

