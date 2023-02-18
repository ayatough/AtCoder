import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

INF = 10**9

def distance(s):
    D = [INF for _ in range(N)]
    Q = []
    D[s] = 0
    heappush(Q, (0, s))
    max_i, max_d = s, 0
    while len(Q) > 0:
        _, q = heappop(Q)
        for p in G[q]:
            if D[q] + 1 < D[p]:
                D[p] = D[q] + 1
                heappush(Q, (D[p], p))
                if max_d < D[p]:
                    max_i, max_d = p, D[p]
    return D, max_i, max_d

D1, s1, _ = distance(0)
_, _, diam = distance(s1)

print(diam + 1)