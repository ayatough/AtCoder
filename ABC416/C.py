from itertools import product

N, K, X = map(int, input().split())

S = []

for _ in range(N):
    S.append(input().strip())

T = []

perms = [range(N)] * K
i = 0

for p in product(*perms):
    t = ""
    for i in p:
        t = t + S[i]
    T.append(t)

T.sort()
print(T[X-1])
