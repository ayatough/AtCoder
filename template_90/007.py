import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

A.sort()

Q = int(input())

for _ in range(Q):
    b = int(input())
    i = bisect_left(A, b)
    if i == 0:
        ans = abs(A[0] - b)
    elif i < N:
        ans = min(abs(A[i-1] - b), abs(A[i] - b))
    else:
        ans = abs(A[-1] - b)
    print(ans)
