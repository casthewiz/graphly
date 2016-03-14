from graphly import *
from searches import *

x = [[1,2],[0,2],[1,0],[4,1],[2,0]]
y = graph(x)
y.output()

z = dfs(x, 0)
print(z)
z = dfs(x, 4)
print(z)
z = dfs(x, 3)
print(z)
