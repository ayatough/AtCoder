from functools import reduce
from collections import Counter
MOD = 10 ** 9 + 7
N, M = map(int, input().split())

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(lambda x, y : x * y % MOD, range(n, n - r, -1))
    under = reduce(lambda x, y : x * y % MOD, range(1,r + 1))
    return over * pow(under, MOD - 2, MOD)

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

cum = 1
for v in C.values():
    cum *= cmb(N+v-1, v)
    cum %= MOD

print(cum)
