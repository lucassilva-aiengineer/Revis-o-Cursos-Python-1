from enum import Enum

# Números enum são números legíveis. Números legendados, que podem ser lidos. 
# Construidos como objeto. 

def constantes():
    class State(Enum):
        INACTIVE = 0
        ACTIVE = 1

    # Uma forma de criar constantes em python
    print(State.ACTIVE)
    print(State(1))
    print(State['ACTIVE'])

    print(State.ACTIVE.value)


    print(list(State))

    print(len(State))
def main():

    constantes()



if __name__ == "__main__":
    main()