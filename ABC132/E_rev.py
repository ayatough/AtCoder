from heapq import heappop, heappush
N, M = map(int, input().split())
link = {(i, j) : [] for i in range(1, N+1) for j in range(3)}
for _ in range(M):
    u, v = map(int, input().split())
    link[(u, 0)].append((v, 1))
    link[(u, 1)].append((v, 2))
    link[(u, 2)].append((v, 0))
S, T = map(int, input().split())

''' dijkstra '''
INF = 10 ** 9
vstd = {(i, j): False for i in range(1, N+1) for j in range(3)}
dist = {(i, j): INF for i in range(1, N+1) for j in range(3)}  # distance
# prev = {i: -1 for i in range(1, N+1)}  # for extract min cost path
pq = []
# initialize
dist[(S, 0)] = 0
heappush(pq, (0, (S, 0)))
while pq:
    _, u = heappop(pq)
    vstd[u] = True
    for v in link[u]:
        if vstd[v]:
            continue
        if dist[u] + 1 < dist[v]:
            dist[v] = dist[u] + 1
            # prev[v] = u
            heappush(pq, (dist[v], v))


print(dist[(T, 0)] // 3 if dist[(T, 0)] % 3 == 0 else -1)
