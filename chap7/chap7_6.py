import sys

def addTo(a, b, k):
    b = [0] * k + b
    cnt = len(a) if len(a) < len(b) else len(b)
    for i in range(cnt):
        b[i] = a[i] + b[i]
    return b

def subFrom(a, b):
    if len(a) < len(b):
        return subFrom(b, a)
    for i in range(len(b)):
        if a[i] < b[i]:
            a[i] = (a[i] + 10) - b[i]
            a[i+1] = a[i+1] - 1
        else:
            a[i] = a[i] - b[i]
    return a

def normalize(C):
    for i in range(len(C)):
        if C[i] >= 10:
            if i == len(C)-1:
                C.append(C[i]//10)
            else :
                C[i+1] = C[i+1] + C[i]//10
            C[i] = C[i] % 10
    return C


def karatsuba(A, B):
    an = len(A)
    bn = len(B)
    if an < bn:
        return karatsuba(B, A)
    if an == 0 or bn == 0:
        return []
    if an == 1 or bn == 1:
        tmp = A[:]
        for i in range(an):
            tmp[i] = A[i]*B[0]
        return  list(tmp)
    half = an // 2
    a0 = A[:half]
    a1 = A[half:]
    if bn < half:
        b0 = B
        b1 = []
    else :
        b0 = B[:half]
        b1 = B[half:]
    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)
    tmp0 = addTo(a0, a1, 0)
    tmp1 = addTo(b0, b1, 0)
    z1 = karatsuba(tmp0, tmp1)
    z1 = subFrom(z1, z0)
    z1 = subFrom(z1, z2)
    C = []
    C = addTo(C, z0, 0)
    C = addTo(C, z1, half)
    C = addTo(C, z2, half+half)
    C = normalize(C)
    return C


sys.setrecursionlimit(10**6)

def hugs(members, fans):
    A = []
    B = []

    for i in members:
        if i == 'M':
            A.append(1)
        else :
            A.append(0)
    for i in reversed(fans):
        if i == 'M':
            B.append(1)
        else :
            B.append(0)
    
    C = karatsuba(A, B)

    allhugs = 0
    for i in range(len(A)-1, len(B)):
        if C[i] == 0 :
            allhugs = allhugs + 1
    
    return allhugs

for i in range(int(input())):
    members = list(input())
    fans = list(input())
    print(hugs(members, fans))
