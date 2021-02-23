# 트리 순회 순서 변경

# 트리 순회 순서에는 전위 순회, 중위 순회, 후위 순회가 있다.
# 전위 : 루트 - 왼쪽 - 오른쪽
# 중위 : 왼쪽 - 루트 - 오른쪽
# 후위 : 왼쪽 - 오른쪽 - 루트 순으로 방문한다.
# 전위와 중위 순회 순서가 주어질 떄, 후위 순회 순서를 출력하라.

# 함수명은 printpostorder.
# 입력은 전위 순회와 중위 순회의 순서.

def postorder(preorder, inorder):

    # 트리에 포함된 총 원소의 수.
    N = len(preorder)
    # 순회 순서가 비었으면 바로 종료.
    if N == 0:
        return []
    # 트리의 루트는 전위 순회의 순서가 루트부터 접근하므로 맨 앞의 원소를 통해 알 수 있음.
    root = preorder[0]
    root_index = inorder.index(root)
    # 전위 순회 순서로부터 루트를 구했으니 중위 순화 순서에서 해당 원소를 찾아 
    # 왼쪽 서브트리와 오른쪽 서브트리로 나눈다.
    left_preorder = preorder[1:root_index+1]
    left_inorder = inorder[:root_index]
    left = postorder(left_preorder, left_inorder)

    right_preorder = preorder[root_index+1:]
    right_inorder = inorder[root_index:]
    right = postorder(right_preorder, right_inorder)
      
    return left + right + root

preorder = [27, 16, 9, 12, 54, 36, 72]
inorder = [9, 12, 16, 27, 36, 54, 72]
print(postorder(preorder, inorder))