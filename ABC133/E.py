import sys
sys.setrecursionlimit(10 ** 5)
MOD = 10 ** 9 + 7
N, K = map(int, input().split())
V = {i: [] for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

def dfs(u, p, c):
    l = len([i for i in V[u] if i != p])
    n = K - 2
    if p == 0:
        n += 1
    if l == 0:
        return c
    for v in V[u]:
        if v == p:
            continue
        c *= dfs(v, u, n)
        n -= 1
        c %= MOD
    return c

print(dfs(1, 0, K))
