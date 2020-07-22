from itertools import combinations

N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append((x, y))

memo = dict()
for (a, b) in combinations(P, 2):
    p, q = a[0] - b[0], a[1] - b[1]
    if p < 0:
        p, q = -p, -q
    elif p == 0 and q < 0:
        q = -q
    if (p, q) in memo:
        memo[(p, q)] += 1
    else:
        memo[(p, q)] = 1

print(N - max(memo.values()) if N > 1 else 1)
