import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())

T = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    T[a].append(b)
    T[b].append(a)

V = list(map(int, input().split()))
W = [False] * (N+1)
for v in V:
    W[v] = True

if len(V) == 1:
    print(1)
else:
    visited = [False] * (N+1)
    q = deque([V[0]])
    def dfs():
        v = q.pop()
        visited[v] = True
        total = W[v]
        for t in T[v]:
            if not visited[t]:
                q.append(t)
                total += dfs()
        return total + 1 if (not W[v] and total != 0) else total
    print(dfs())
