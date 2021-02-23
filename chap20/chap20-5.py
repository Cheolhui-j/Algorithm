# 요새

# 입력으로 주어진 성벽의 위치와 크기를 통해 
# 가장 멀리 있는 두 성벽의 거리를 반환함.
# 이 때, 성벽의 두께는 편의상 0으로 가정.

# 함수명은 height. 
# 입력으로 성벽 간의 포함관계를 나타낸 
# 트리가 인가됨.
# 출력은 가장 거리가 먼 두 지점 사이의 거리.




n = 3
x = [5,5,5]
y = [5,5,5]
radius = [5,10,15]

# 함수명은 getTree.
# 입력으로 성벽들의 번호가 인가됨. 
# 출력은 성벽들의 포함관계를 나타낸 트리. 
class TreeNode(object):
    def __init__(self):
        self.node = []

    def add_node(self, val):
        self.node.append(val)

def getTree(root):
    tree = TreeNode()
    for i in range(n):
        if isChild(root, ch):
            TreeNode.add_node(getTree(ch))
    return tree

def enclose(a, b):
    return (radius[a] > radius[b]) and ((pow(y[a]-y[b], 2) + pow(x[a]-x[b],2)) < pow(radius[a]-radius[b], 2))

def isChild(parent, child):
    if not enclose(parent, child):
        return False
    for i in range(n):
        if i != parent and i!= child and enclose(parent, i) and enclose(i, child):
            return False
    return True

tree = getTree()