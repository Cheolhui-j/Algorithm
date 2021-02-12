# 외계 신호 분석.

# 일정 수열을 입력받아 해당 수열의 부분 수열의 합이
# 특정 값이 되는 부분 수열의 개수를 반환.

# 임의의 수 init을 받아
# 특정 규칙에 따라 난수를 발생시키는 함수 RNG
def RNG(init):
    init = (((init * 214013) + 2531011) % pow(2,32)) 
    return (init % 10000 + 1)

# 함수명은 countRanges.
# 입력은 일정 수열의 길이, 부분 수열의 특정 합.
# 출력은 입력 수열의 부분 수열의 합 중 특정 값을 만족하는 부분 수열의 수.
def countRanges(n, k):
    # 입력으로 들어갈 수열, 부분 수열 합을 1983으로 초기화. 
    newSignal = 1983
    rangeSignal = [newSignal]
    ret = 0
    rangeSum = newSignal

    for _ in range(n):
        # 한 번 구간을 돌 때마다 임의의 난수를 생성하고
        # 구간에 값을 추가 및 부분 수열 합에 더해줌.
        newSignal = RNG(newSignal)
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



