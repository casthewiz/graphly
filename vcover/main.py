from graphly import *
from searches import *

x = [[1,2],[0,2],[1,0],[4,1],[2,0]]
# y = graph(x)
# y.generate(200000)
# y.output()
# y.inverse()
# y.output()

z = graph(x)
z.fImport("sample_2.txt")

#print("Starting Graph:")
#z.output()

#print("\nProcess:")
while z.isEdgeLeft():
    edge = z.selectRandEdge()
    z.removeEdge(edge)
    z.addEdgeToSolution(edge)
#print("\nEnding Graph:")
#print("No Remaining Connections")
#z.output()

g = set()
for i in range(0, z.size):
    g.add(i)
inverse = g - z.indSet
z.indSet = inverse

print("\nSolution:")

print(z.indSet)
