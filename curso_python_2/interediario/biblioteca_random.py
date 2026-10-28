import random

# Biblioteca random

# Números decimais entre 1 e 10, incluindo o e o 10 
a = random.uniform(1, 10)
print(a)


# Um número inteiro entre 1 e 10, incluindo o 1 e o 10 
b = random.randint(1, 10)


# Um número inteiro entre 1 e 10, não incluso o 10. 

c = random.randint(1, 10)
print(b)


# Uma distribuição normal (Poisson)
d = random.normalvariate(0, 1) 
print(d)


# Minha lista
lista_letras= list("ABCDEFG")
letra = random.choice(lista_letras)
print(letra)

# Uma fração da lista original
parte_lista = random.sample(lista_letras, 2)
print(parte_lista)

letras = random.choices(lista_letras, k= 3)
print(letras)


# Embaralhando uma lista

random.shuffle(letras)
print(letras)