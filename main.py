from graphly import *
from searches import *

x = [[1,2],[0,2],[1,0],[4,1],[2,0]]
# y = graph(x)
# y.generate(100)
# y.output()
# y.inverse()
# y.output()

z = graph(x)
z.fImport("sample_1.txt")
z.inverse()
z.output()
