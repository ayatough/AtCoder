from math import sqrt

N = int(input())
A = list(map(int, input().split()))

P = []

Primes = []

M = 10 ** 5

tbl = [True] * (M + 1)
tbl[0] = tbl[1] = False

for i in range(2, int(sqrt(M)+0.5)):
    p = i * 2
    while p <= M:
        tbl[p] = False
        p += i

for i, t in enumerate(tbl):
    if t:
        Primes.append(i)

for a in A:
    n = 0
    m = int(sqrt(a) + 0.5)
    for p in Primes:
        if p > m:
            break
        while a % p == 0:
            n += 1
            a //= p

    if a != 1:
        n += 1

    P.append(n)

grundy = P[0]

for p in P[1:]:
    grundy ^= p

print("Anna" if grundy else "Bruno")
