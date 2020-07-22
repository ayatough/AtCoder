from itertools import combinations
from bisect import bisect
N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i, j in combinations(range(1,N), 2):
    # a <= b <= c
    b, c = L[i], L[j]
    k = bisect(L, c-b)
    ans += max(0, i-k)

print(ans)
