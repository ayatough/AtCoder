import sys
from functools import lru_cache
input = sys.stdin.readline
N, M = map(int, input().split())
INF = float('inf')
V = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    V[s-1].append(t-1)

dp = [[0] * N for _ in range(2)]

@lru_cache(maxsize=None)
def dfs(u, cn):
    if u == N-1:
        return 0
    if u > cn and dp[0][u]:
        dp[1][u] = dp[0][u]
        return dp[1][u]
    e = 0
    emax = 0
    c = 0
    for v in V[u]:
        e += dfs(v,cn) + 1
        emax = max(emax,e)
        c+=1
    if u==cn:
        if c == 1:
            dp[cn>=0][u] = INF
        else:
            dp[cn>=0][u] = (e-emax)/(c-1)
    else:
        dp[cn>=0][u] = e/c
    return dp[cn>=0][u]

ans = dfs(0, -1)
for i in range(N-2,-1,-1):
    ans = min(ans, dfs(0,i))

print(ans)
