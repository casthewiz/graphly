from graphly import *



def findSet():
    x = graph()
    # x.fImport("sample_1.txt")
    x.cmdImport()
    x.solution()
    return 0
findSet()
print("Press 'n' if finished.")

while input() is not 'n':
    x.cmdImport()
    findSet()
    print("Press 'n' if finished.")
