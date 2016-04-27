from random import *

class node:
    index = -1
    children = {}

    def __init__(self, index, children):
        self.index = index
        self.children = children

    def set(self, child):
        self.children.add(child)

    def output(self):
        print(str(self.index) + " " + str(self.children))

# Notes about graphly

class graph:
    # bucket is the container for all nodes
    bucket = []
    # indSet is the solution container
    indSet = set()
    size = 0

    # takes in size
    def __init__(self, qArray = list()):
        self.bucket = [node(ind, i) for ind, i in enumerate(qArray)]
        self.size = len(self.bucket)

    def output(self):
        for i in self.bucket:
            i.output()

    def indSetOutput(self):
        print(" ".join(str(i) for i in self.indSet))

    def solution(self):
        while self.isEdgeLeft():
            edge = self.selectRandEdge()
            self.removeEdge(edge)
            self.addEdgeToSolution(edge)
        g = set()
        for i in range(0, self.size):
            g.add(i)
        inverse = g - self.indSet
        self.indSet = inverse
        self.indSetOutput()
        return 0


    #returns a random existing edge of the form [P1, P2]
    #sample usage: z.randEdge()
    #returns: [61, 22]
    def selectRandEdge(self):
        bucket2 = []
        for val in self.bucket:
            if val:
                if len(val.children) > 0:
                    bucket2.append(val)

        #grab a random point from the bucket, an object
        randP1 = choice(bucket2)

        #grab a random child of that point, an int
        randP2 = choice(tuple(randP1.children))

        #grab the index of the initial point, an int
        randP1 = randP1.index

        #combine into an edge
        randE = []
        randE = [randP1, randP2]

        #DEBUG - uncomment below for a random edge
        #print("Selected Edge: " + str(randE))
        return randE



    #adds an edge to the solution
    #sample usage z.addEdgeToSolution(z.selectRandEdge())
    #indSet becomes: {0, 7}
    def addEdgeToSolution(self, edge):
        #add first point to set
        self.indSet.add(edge[0])

        #add second point to set
        self.indSet.add(edge[1])

        #DEBUG - uncomment below for the current solution
        #print("Current Inverse Solution: " + str(self.indSet))
        return 0



    #adds a point to the solution
    #sample usage z.addPointToSolution(4)
    #indSet becomes: {4}
    def addPointToSolution(self, point):
        #adds point to set
        self.indSet.add(point)
        #print("Current Inverse Solution: " + str(self.indSet))
        return 0


    def removePoint(self, point):
        #print("Removing Point: " + str(point))

        #DEBUG - uncomment below to see graph before removal
        #print("\nBefore Removal: ")
        #self.output()

        #for each value that is in the points set...
        #visit that point node and remove the child which
        #connects to the passed in point
        for val in self.bucket[point].children:
            self.bucket[val].children.remove(point)

        self.bucket[point] = None

        #DEBUG - uncomment below to see graph after removal
        #print("\nAfter Removal: ")
        #self.output()

        #print("Removed Point: " + str(point))
        return 0

    def removeEdge(self, edge):
        self.removePoint(edge[0])
        self.removePoint(edge[1])
        return 0

    def isEdgeLeft(self):
        for node in self.bucket:
            if node:
                if len(node.children) > 0:
                    return True
        return False
    #size determines the number of nodes in a given graph
    #connectivity is the average factor of nodes connected - e.g .10 is a node will connect to 10% of the graph.
    #variation is the degree of entropy for connections - e.g. .50 means that the connectivity for a given node will vary within 50% of it's given value
    #WARNING - connectivity or variation should not exceed 1.0 !
    def generate(self, size = 10, connectivity=.10, variation=.50):
        g = list()
        for i in range(0, size):
            sub = {}
            connectionFlux = (variation * connectivity)
            connectionFactor = round(uniform(0 - connectionFlux, connectionFlux), 2) + connectivity
            connectionNumber = size * connectivity
            for j in range(0, int(connectionNumber)):
                sub.add(randrange(0, size))
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

    def nextElem(self, i):
        if (i):
            tmp = i.pop()
            i.add(tmp)

            return tmp

    def bron_kebrosch(self, clique, candidates = set(), excluded = set()):
        if not candidates and not excluded:
            self.indSet.union(set(clique))
        pivot = self.nextElem(candidates) or self.nextElem(excluded)
        for i in list(candidates.difference((self.bucket[pivot].children))):
            self.bron_kebrosch(clique + [i], candidates.intersection(self.bucket[i].children), excluded.intersection(self.bucket[i].children))
            candidates.remove(i)
            excluded.add(i)


    def iter_bron_kebrosch(self):
        candidates = set(range(1, self.size))
        clique = []
        graph = self.bucket
        S = []
        S.append(list())
        S.append(candidates)
        S.append(set())
        while S:
            excluded = S.pop()
            candidates = S.pop()
            clique = S.pop()
            if not candidates and not excluded:
                self.indSet = set(clique)
                break
            if candidates:
                i = self.nextElem(candidates) or self.nextElem(excluded)
                candidates.remove(i)
                S.append(clique)
                S.append(candidates)
                S.append(excluded.add(i))
                #########################
                S.append(clique + [i])
                S.append(candidates.intersection(graph[i].children))
                S.append(excluded.intersection(graph[i].children))

    def tree_set(self):
        return 0

    def fExport(self):
        return 0

    def cmdImport(self):
        self.bucket = []
        print("Starting command line input mode - input is line by line, per line.")
        print("Awaiting standard input.")
        first = input()
        for i in range (0, int(first)):
            x = input()
            x = x.split()
            x.pop(0)
            y = {int(j) for j in x}
            self.bucket.append(node(i, y))
        self.size = len(self.bucket)
        return 0

    def fImport(self, fname):
        self.bucket = []
        f = open(fname, 'r')
        first = f.readline()
        for i in range (0, int(first)):
            x = f.readline()
            x = x.split()
            x.pop(0)
            y = {int(j) for j in x}
            self.bucket.append(node(i, y))
        self.size = len(self.bucket)
