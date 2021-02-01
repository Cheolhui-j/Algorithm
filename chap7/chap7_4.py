import sys

def solve(h, left, right):
    if left == right:
        return h[left]
    mid = (left+right)//2
    ret = max(solve(h, left, mid), solve(h, mid+1, right))
    lo = mid
    hi = mid+1
    height = min(h[lo], h[hi])
    ret = max(ret, height * 2)
    while left < lo or hi < right:
        if hi < right and (lo == left or h[lo - 1] < h[hi + 1]):
            hi = hi + 1
            height = min(height, h[hi])
        else :
            lo = lo - 1
            height = min(height, h[lo])
        ret = max(ret, (hi-lo+1) * height)
    return ret

sys.setrecursionlimit(10**6)

for i in range(int(input())) :
    h = [int(a) for a in input()]
    print(solve(h, 0, len(h)-1))