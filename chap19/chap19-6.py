# 외계 신호 분석.

# 일정 수열을 입력받아 해당 수열의 부분 수열의 합이
# 특정 값이 되는 부분 수열의 개수를 반환.

# 임의의 수 init을 받아
# 특정 규칙에 따라 난수를 발생시키는 클래스 RNG
# seed 값과 결과로 나온 랜덤 값은 별개이므로
# 이를 구분하기 위해 class형태로 만들어 class변수에
# seed 값을 따로 저장함. 초반에 좀 헤맴.
class RNG(object):
    def __init__(self, seed):
        self.seed = seed
    def renew(self):
        self.seed = (((self.seed * 214013) + 2531011) % pow(2,32)) 
    def getvalue(self):
        return (self.seed % 10000 + 1)

# 함수명은 countRanges.
# 입력은 일정 수열의 길이, 부분 수열의 특정 합.
# 출력은 입력 수열의 부분 수열의 합 중 특정 값을 만족하는 부분 수열의 수.
def countRanges(n, k):
    # 입력으로 들어갈 수열, 부분 수열 합을 1983으로 초기화. 
    seed = RNG(1983)
    newSignal = seed.getvalue()
    rangeSignal = [newSignal]
    ret = 0
    rangeSum = newSignal

    for _ in range(n):
        # 한 번 구간을 돌 때마다 임의의 난수를 생성하고
        # 구간에 값을 추가 및 부분 수열 합에 더해줌.
        seed.renew() 
        newSignal = seed.getvalue()
        rangeSum = rangeSum + newSignal
        rangeSignal.append(newSignal)

        # 구간의 합이 특정 합 k를 초과하는 경우, 
        # k보다 작아질 때까지 뺀다.
        while rangeSum > k:
            rangeSum = rangeSum - rangeSignal[0]
            rangeSignal.pop(0)
        
        # 작아진 값이 k를 만족할 경우,
        # 결과값에 1을 추가.
        if rangeSum == k:
            ret = ret + 1

    return ret

print(countRanges(5000, 5265))



