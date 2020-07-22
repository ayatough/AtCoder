from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N, K = map(int, input().split())
MOD = 10 ** 9 + 7

for i in range(1, K+1):
    if i > N-K+1:
        print(0)
        continue
    a = cmb(N-K+1, i)
    a %= MOD
    b = cmb(K-1, i-1)
    b %= MOD
    print((a * b)%MOD)
