from random import *

class node:
    index = -1
    children = []

    def __init__(self, index, children):
        self.index = index
        self.children = children

    def set(self, child):
        self.children.append(child)

    def output(self):
        print(str(self.index) + " " + str(self.children))

# Notes about graphly

class graph:
    # bucket is the container for all nodes
    bucket = []
    size = 0

    # takes in size
    def __init__(self, qArray):
        self.bucket = [node(ind, i) for ind, i in enumerate(qArray)]
        self.size = len(self.bucket)

    def output(self):
        for i in self.bucket:
            i.output()

    #size determines the number of nodes in a given graph
    #connectivity is the average factor of nodes connected - e.g .10 is a node will connect to 10% of the graph.
    #variation is the degree of entropy for connections - e.g. .50 means that the connectivity for a given node will vary within 50% of it's given value
    #WARNING - connectivity or variation should not exceed 1.0 !
    def generate(self, size = 10, connectivity=.10, variation=.50):
        g = list()
        for i in range(0, size):
            sub = []
            connectionFlux = (variation * connectivity)
            connectionFactor = round(uniform(0 - connectionFlux, connectionFlux), 2) + connectivity
            connectionNumber = size * connectivity
            for j in range(0, int(connectionNumber)):
                sub.append(randrange(0, size))
            g.append(sub)
        newGraph = graph(g)
        self.bucket = newGraph.bucket
        self.size = newGraph.size
        return 0


    def inverse(self):
        g = set()
        for i in range(0, self.size):
            g.add(i)
        for i in range(0, self.size):
            compare = set(self.bucket[i].children)
            inverse = g - compare
            self.bucket[i].children = inverse
        return 0

    def fExport(self):
        return 0

    def fImport(self, fname):
        return 0
