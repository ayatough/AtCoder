import sys
sys.setrecursionlimit(10 ** 5)

N, M = map(int, input().split())
V = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    V[x].append(y)

dp = [None for _ in range(N)]

def dfs(x):
    if dp[x] is not None:
        return dp[x]
    if not V[x]:
        dp[x] = 0
        return 0
    l = max(dfs(v) for v in V[x]) + 1
    dp[x] = l
    return l

print(max(dfs(v) for v in range(N)))
