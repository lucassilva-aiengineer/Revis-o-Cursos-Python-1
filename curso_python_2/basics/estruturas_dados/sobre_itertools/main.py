from itertools import product 

a = [1, 2]
b = [3, 4]

prod = product(a, b)
print(list(prod))

prod_a = product(a, b, repeat= 2)
print(list(prod_a))