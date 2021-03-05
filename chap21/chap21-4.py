
class Binery_Tree(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.size = 1
    
    def setleft(self, node):
        self.left = node
        if self.left is not None:
            self.size = self.size + self.left.size

    def setright(self, node):
        self.right = node
        if self.right is not None:
            self.size = self.size + self.right.size

def getTree(x, y):

    if x is None or y is None:
        return None

    tree = Binery_Tree(x[0], y[0])

    return tree
        
x = [72, 57, 74, 64]
y = [50, 67, 55, 60]

tree = getTree(x, y)

def isDominated(x, y, node):

    if node.x < x and node.y < y:
        return 'Dominate'

    elif node.x > x and node.y > y:
        return 'Dominated'
        
    else :
        return 'merge'
