from collections import Counter

N = int(input())

def factorize(n):
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

def factor_factorize(n, d):
    if n == 1:
        return d
    d.extend(factorize(n))
    return factor_factorize(n-1, d)

F = Counter(factor_factorize(N, []))

# (4, 4, 2), (14, 4), (24, 2), (74,)
cases = []

n1 = [True for v in F.values() if v >= 4].count(True)
m1 = [True for v in F.values() if 4 > v >= 2].count(True)
cases.append(n1 * (n1-1) // 2 * max(0, m1+n1-2))

n2 = [True for v in F.values() if v >= 14].count(True)
m2 = [True for v in F.values() if 14 > v >= 4].count(True)
cases.append(n2 * max(0, m2+n2-1))

n3 = [True for v in F.values() if v >= 24].count(True)
m3 = [True for v in F.values() if 24 > v >= 2].count(True)
cases.append(n3 * max(0, m3+n3-1))

n4 = [True for v in F.values() if v >= 74].count(True)
cases.append(n4)

print(sum(cases))
