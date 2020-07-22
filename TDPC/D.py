from collections import Counter
from math import log
N, D = map(int, input().split())

def gfct(M):
    C = Counter()
    def fct(m):
        if m < 2:
            return 1
        r = m
        for i in range(2, int(m**0.5)+1):
            if m % i == 0:
                r = i
                break
        C.update([r])
        return m // r

    m = fct(M)
    while m != 1:
        m = fct(m)
    return C

C = gfct(D)
if max(C.keys()) <= 5:
    dp = [[[[0 for _ in range(C[5]+1)] for _ in range(C[3]+1)] for _ in range(C[2]+1)] for _ in range(N+1)]

    dp[0][0][0][0] = 1

    lut = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [2, 0, 0], [0, 0, 1], [1, 1, 0]]

    for i in range(1,N+1):
        for a in range(C[2]+1):
            for b in range(C[3]+1):
                for c in range(C[5]+1):
                    for l in lut:
                        dp[i][min(a+l[0],C[2])][min(b+l[1],C[3])][min(c+l[2],C[5])] += dp[i-1][a][b][c] * 1/6

    print(dp[-1][-1][-1][-1])
else:
    print(0)
