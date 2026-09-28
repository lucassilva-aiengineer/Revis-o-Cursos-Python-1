# Decoradores 

# Uma maneira de modificarmos o comportamento interno de uma função 


def logtime(func):
    def wraper():

        print("before")
        val = func()
        print("depois") 
        return val 

    return wraper 


@logtime
def hello():
    print("Hello!")


hello()