class Tree(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.size = 1
    
    def setleft(self, node):
        assert isinstance(node, Tree)
        self.left = node
        self.calcsize()

    def setright(self, node):
        assert isinstance(node, Tree)
        self.right = node

    def calcsize():
        if self.left is not None:
            self.size = self.size + self.left.size
        if self.right is not None:
            self.size = self.size + self.right.size

def isDominated(x, y):


