# Namedtuple 
# Tuplas nomeadas: Uma forma de criarmos estruturas de dados nomeadas de forma bastante ágil. 

from collections import namedtuple 
Point = namedtuple('Point', 'x,y')

pt = Point(1, -4) # 
print(pt.x)

soma = pt.x + pt.y

print(soma)