import sys
input = sys.stdin.readline

N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split()))

lo, hi = 1, L // (K+1) + 1

def judge(v):
    ret = False
    cum = 0
    pre = 0
    i, j = 1, 0
    i_pre = 0
    while i < N+1 and j < K:
        if A[i] - A[i_pre] < v:
            i += 1
            continue
        i_pre = i
        i += 1
        j += 1
    if L - A[i_pre] >= v and j >= K:
        ret = True
    return ret

while lo < hi - 1:
    mi = (hi + lo) >> 1
    if judge(mi):
        lo = mi
    else:
        hi = mi

print(lo)
