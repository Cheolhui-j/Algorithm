import sys

clock_switch = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]

def check_clock(current_clock, current_switch):
    for i in current_switch:
        current_clock[i] = current_clock[i] + 3
        if current_clock[i] == 15:
            current_clock[i] = 3 
    return current_clock

def clock(current_clock, sw_cnt):
    if sw_cnt == 10:
        if sum(map(lambda x: x % 12, current_clock)) == 0:
            return 0
        else :
            return sys.maxsize 
    ret =  sys.maxsize
    for j in range(4):
        ret = min(ret, j + clock(current_clock, sw_cnt + 1))
        current_clock = check_clock(current_clock, clock_switch[sw_cnt])
    return ret

sys.setrecursionlimit(10**6)
# test case 개수를 입력으로 받음.
for T in range(int(input())):
    current_clock = list(map(int, input().split()))
    print(clock(current_clock, 0))