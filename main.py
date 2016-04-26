from graphly import *
from searches import *

x = [[1,2],[0,2],[1,0],[4,1],[2,0]]
# y = graph(x)
# y.generate(200000)
# y.output()
# y.inverse()
# y.output()

z = graph(x)
z.fImport("sample_1.txt")
# z.output()
z.inverse()
# z.output()


# z.bron_kebrosch(clique = list(), candidates = set(range(1, z.size)))
z.iter_bron_kebrosch()
print(z.indSet)
