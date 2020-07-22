# from bisect import bisect_left
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

resid = M
i = 0
pi = 0
pif = True
while resid:
    A[i] //= 2
    resid -= 1
    if i < N-1 and A[i] < A[i+1]:
        if A[pi] > A[i+1]:
            A.sort(reverse=True)
            i = 0
            pi = 0
            pif = True
            continue
        if pif:
            pi = i
            pif = False
        i += 1
    else:
        i = pi
        pif = True

print(sum(A))
