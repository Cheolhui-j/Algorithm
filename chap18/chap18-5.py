# 조세푸스 문제

# 임의의 총 인원 수 N이 주어지고 1번 사람부터 자결을 시작해 
# 1번 사람을 기준으로 k번째 사람이 다음으로 자결할 떄
# 맨 마지막 두 사람이 되려면 몇번째여야 되는가?

# 함수명 joseps로 하고 
# 입력은 총 인원의 상태를 나타내는 whokill list, 간격 K를 받고 
# 출력은 살아남는 사람의 번호로 하면 될 듯
# 인원 수 만큼 list를 1로 초기화
# 1은 생존, 0은 자결을 의미.
def joseps(whokill, start, K):

    if len(whokill) == 2:
        return whokill
    
    del whokill[start-1]

    renew = (K + start) % len(whokill)
    
    joseps(whokill, renew, K)    

        
whokill = list(range(6))
k = 3
joseps(whokill, 1, k)