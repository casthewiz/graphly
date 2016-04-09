
class node:
    index = -1
    children = []

    def __init__(self, index, children):
        self.index = index
        self.children = children

    def set(self, child):
        self.children.push(child)

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

    def generate(self):

        return 0

    def fExport(self):
        for i in self.bucket:
            open()
        return 0

    def fImport(self, fname):
        return 0
