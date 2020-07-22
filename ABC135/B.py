N = int(input())
P = list(map(int, input().split()))

Q = P.copy()
Q.sort()

n = [p == q for (p, q) in zip(P, Q)].count(False)
print('YES' if n <= 2 else 'NO')
