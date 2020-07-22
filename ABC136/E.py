N, K = map(int, input().split())
A = list(map(int, input().split()))
INF = (10 ** 6)*500

M = sum(A)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

T = make_divisors(M)

ans = INF
for t in T:
    p = []
    for a in A:
        p.append(a - a//t * t)
    p.sort()
    s, w = 0, 0
    for h in p:
        if s + h <= K:
            s += h
        else:
            w += t - h
    if s >= w:
        ans = t
        break

print(ans)
