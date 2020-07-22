from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))
A.sort()
F.sort(reverse=True)

lo, hi = 0, max(a*f for (a, f) in zip(A,F))
while lo < hi:
    mid = (lo + hi)//2
    rsd = K
    possible = True
    for a, f in zip(A,F):
        rsd -= ceil(max(a*f-mid, 0)/f)
        if rsd < 0:
            possible = False
            break
    if possible:
        hi = mid
    else:
        lo = mid+1

print(lo)
