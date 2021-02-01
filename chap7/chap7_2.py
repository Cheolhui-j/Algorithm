import sys

# 쿼드 트리 리스트를 입력으로 받아 상하가 반전된 값을 출력.
def reverse(quad):
    # quad 인자가 iterator이기 때문에 next함수를 통해 다음 iter로 옮김.
    current = next(quad)
    # 기저 사례 : 현재 iter에서의 값이 'w' 또는 'b'일 경우, 값을 그대로 반환.
    if current == 'w' or current == 'b':
        return current
    # 'w' 나 'b' 가 아닌 x인 경우, 아래의 네개의 과정을 거침
    # 'w' 나 'b'인 경우, 그 값을 반환하고 다음 iter로 전진시킴.
    lefttop = reverse(quad)
    righttop = reverse(quad)
    leftbottom = reverse(quad)
    rightbottom = reverse(quad)
    # 구해진 값들에 대해 상하를 반전시켜 병합.
    return 'x' + leftbottom + rightbottom + lefttop + righttop

for T in range(int(input())):
    # 입력을 받는다.
    quad = input()
    # reverse 함수를 사용해 값을 출력한다.
    print(reverse(iter(list(quad))))