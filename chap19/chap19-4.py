# 짝이 맞지 않는 괄호 문제

# 입력으로 일련의 괄호들이 들어올 때
# 해당 괄호들의 짝 순서가 맞는지를 확인하여   
# 짝 순서가 맞으면 Yes를, 맞지 않으면 No를 반환.

# 함수명은 wellMatched.
# 입력은 일련의 괄호가 나열된 문자열.
# 출력은 Yes, 혹은 No.
def wellMatched(formula):
    # 여는 괄호를 나열한 opening.
    opening = '({['
    # 닫는 괄호를 나열한 closing.
    closing = ')}]'
    # 열린 괄호들을 담는 openStack.
    openStack = []
    for i in range(len(formula)):
        # 여는 괄호인지 닫는 괄호인지 확인.
        if opening.find(formula[i]) != -1:
            # 여는 괄호이므로 openStack에 추가.
            openStack.append(formula[i])
        else :
            # 나머지 경우
            # 열린 괄호가 없는 경우
            if len(openStack) == 0:
                return False
            # 짝이 맞지 않는 경우
            if opening.find(openStack[-1]) != closing.find(formula[i]):
                return False 
            # 짝을 확인한 경우 제외.
            openStack.pop()

    return len(openStack) == 0

formula = '({}[(){}])'
print(wellMatched(formula))