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
#z.output()
#edge = z.selectRandEdge()
#z.addEdgeToSolution(edge)
#z.removeEdge(edge)
#z.output()
#print(str(z.isEdgeLeft()))

while z.isEdgeLeft():
    edge = z.selectRandEdge()
    z.addEdgeToSolution(edge)
    z.removeEdge(edge)
g = set()
for i in range(0, self.size):
    g.add(i)
inverse = g - z.indSet
z.indSet = inverse
print(z.indSet)
