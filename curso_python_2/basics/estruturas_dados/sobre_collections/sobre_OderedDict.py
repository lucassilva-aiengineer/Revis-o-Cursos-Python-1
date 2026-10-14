# Collections: OderedDict 

from collections import OrderedDict 

dicionario_ordenado = OrderedDict()
dicionario_ordenado['b'] = 2 
dicionario_ordenado['c'] = 3 
dicionario_ordenado['d'] = 4 
dicionario_ordenado['a'] = 1 

print(dicionario_ordenado)


# defaultdict
from collections import defaultdict 

# Um defaultdict, dicionário padrão, é um dicionário que cria automáticamente uma 
# chave caso a chave buscada ainda não esteja no dicionário. 


# d = defaultdict(float)
d = defaultdict(list)
# d = defaultdict(int)
d['a'] = 1
d['b'] = 20

print("Chave a: ", d['a'])
print("Chave b: ", d['b'])

print("Chave c: ", d['c'])

# Deque 
# Onde podemos manipular a adição (remoção) de elementos em suas extremidades
from collections import deque 

# d = {}

# Uma estrutura de dados muito interessante
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)

print(d)

# d.pop()
# print(d)

d.popleft()
# d.popright()
print(d)

# d.clear()

d.extend([10, 20, 30])

d.extendleft([15, 50, 30])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)
