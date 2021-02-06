# 조세푸스 문제

# 임의의 총 인원 수 N이 주어지고 1번 사람부터 자결을 시작해 
# 1번 사람을 기준으로 k번째 사람이 다음으로 자결할 떄
# 맨 마지막 두 사람이 되려면 몇번째여야 되는가?

# 함수명 joseps로 하고 
# 입력은 총 인원의 상태를 나타내는 whokill list, 시작 위치, 간격 K를 받고 
# 출력은 살아남는 사람의 번호로 하면 될 듯.
def joseps(whokill, start, K):

    # 기저 사례 : list 길이가 2라면 반환.
    if len(whokill) == 2:
        return whokill
    
    # start 위치의 list원소를 제거.
    del whokill[start]

    # 다음 자결할 사람의 위치를 계산.
    # 이 때, 주의할 건 남은 인원들 중 위치를 계산하는 것이므로 -1이 필요.
    # 이유는 위의 delete를 통해 한 사람이 사라졌고 
    # 그 위치를 다음 사람이 받아서 다음 위치를 계산하기 때문에 자연적으로 
    # 위치값에 1이 더해진다고 볼 수 있음. 많이 헤맴.
    renew = (K + start - 1) % len(whokill)

    # 재귀호출로 loop를 해결.
    survivor = joseps(whokill, renew, K)    

    return survivor

# 총 인원 N, 건너뛸 값 K.
N = 8
k = 3
# 1부터 입력 크기까지의 list를 초기화함.
whokill = list(range(1, N + 1))
# 계산파트.
survivor = joseps(whokill, 0, k)
print(survivor)
