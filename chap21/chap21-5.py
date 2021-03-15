# 요새

# 입력으로 주어진 성벽의 위치와 크기를 통해 
# 가장 멀리 있는 두 성벽의 거리를 반환함.
# 이 때, 성벽의 두께는 편의상 0으로 가정.

# n = 8
# x = [21,15,13,12,19,30,32,32]
# y = [15,15,12,12,19,24,10,9]
# radius = [20,10,5,3,2,5,7,4]

n = 3
x = [5,5,5]
y = [5,5,5]
radius = [15,10,5]

# 함수명은 getTree.
# 입력으로 성벽들의 번호가 인가됨. 
# 출력은 성벽들의 포함관계를 나타낸 트리.
# 

class Tree(object):
    "Generic tree node."
    def __init__(self, data='root'):
        self.data = data
        self.children = []
    def add_child(self, node):
        self.children.append(node) 

def getTree(root):
    tree = Tree(root)
    for i in range(n):
        if isChild(root, i):
            tree.add_child(getTree(i))
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


# tree = getTree(0)
# tree

# 함수명은 height. 
# 입력으로 성벽 간의 포함관계를 나타낸 
# 트리가 인가됨.
# 출력은 가장 거리가 먼 두 지점 사이의 거리.
def height(root):

    heights = []

    longest = 0

    for i in range(len(root.children)):
        heights.append(height(root.children[i])[0])

    if len(heights) == 0:
        return [0, 0]

    heights.sort(reverse=True)

    if len(heights) >= 2:
        longest = max(longest, 2 + heights[1] + heights[0])

    return [heights[0] + 1, longest]

def solve(root):
    #longest = 0

    h, longest = height(root)

    longest = max(h, longest)

    return longest


root = getTree(0)
print(solve(root))