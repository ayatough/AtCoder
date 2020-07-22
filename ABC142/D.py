from fractions import gcd
from collections import Counter
A, B = map(int, input().split())
F = gcd(A, B)

# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

C = Counter(prime_factorize(F))

print(len(C)+1)
