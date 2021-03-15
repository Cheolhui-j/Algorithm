class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = None
        self.right = None
        self.size = 1

class Binery_Tree(object):
    def __init__(self):
        self.node = None
        self.size = 0
    
    def insert(self, tree, node):

        if tree.node is None:
            tree.node = node
            tree.size = tree.size + 1

        else:
            if tree.node.x > node.x:
                if tree.left is not None:
                    tree.insert(tree.left, node)
                else :
                    tree.left = node
                    tree.size = tree.size + tree.left.size
            if tree.noded.x < node.x:
                if tree.right is not None:
                    tree.insert(tree.right, node)
                else :
                    tree.right = node
                    tree.size = tree.size + tree.right.size

    def delete(self, node):



x = [72, 57, 74, 64]
y = [50, 67, 55, 60]

def getTree(x, y):

    if x is None or y is None:
        return None

    tree = Binery_Tree()

    for i in range(0, len(n)-1):

        tree.insert(Node(x[i], y[i]))

        if tree.x > x[i+1] and tree.y > y[i+1]:
            continue
        elif tree.x < x[i+1] and tree.y < y[i+1]:
            tree.swapNode(tree.root, Node(x[i+1], y[i+1])
        else:
            tree.insert(Node(x[i+1], y[i+1]))

    return tree
