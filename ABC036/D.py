import sys
from collections import deque
from operator import mul
from itertools import accumulate
sys.setrecursionlimit(10 ** 5)
MOD = 10 ** 9 + 7
N = int(input())
V = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

dp = {i: [0, 0] for i in range(1,N+1)}

def dfs(u, w):
    if dp[u][0] != 0:
        return dp[u]
    bl, wh = 1, 1
    for v in V[u]:
        if v == w:
            continue
        bl *= dfs(v, u)[0]
        bl %= MOD
        wh *= dfs(v, u)[1]
        wh %= MOD
    dp[u] = [(bl + wh) % MOD, bl]
    return dp[u]

print(dfs(1, 0)[0])

# dp[1] = [1, 1]
# q = deque()
# q.append(1)
# vstd = {i: False for i in range(1,N+1)}
# while len(q) > 0:
#     u = q.popleft()
#     vstd[u] = True
#     for v in V[u]:
#         if v == u or vstd[v]:
#             continue
#         q.append(v)
#         dp[v][0] += dp[u][1]
#         dp[v][1] += (dp[u][0] + dp[u][1])
