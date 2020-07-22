from heapq import heappop, heappush
N, M = map(int, input().split())
V = [[] for _ in range(N)]
for i in range(1,N):
    V[i].append((i-1, 0))
for _ in range(M):
    l, r, c = map(int, input().split())
    V[l-1].append((r-1, c))
INF = float('inf')

q = [(0, 0)]
d = [INF] * N
d[0] = 0

while q:
    _, u = heappop(q)
    for v, c in V[u]:
        if d[v] > d[u] + c:
            d[v] = d[u] + c
            heappush(q, (d[v], v))

print(d[-1] if d[-1] != INF else -1)
