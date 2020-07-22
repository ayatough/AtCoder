from heapq import heappop, heappush
N, M = map(int, input().split())
link = {i: [] for i in range(1, N+1)}
for _ in range(M):
    u, v = map(int, input().split())
    link[u].append(v)
S, T = map(int, input().split())

''' dijkstra '''
INF = 10 ** 9
vstd = {i: False for i in range(1, N+1)}
dist = {i: INF for i in range(1, N+1)}  # distance
# prev = {i: -1 for i in range(1, N+1)}  # for extract min cost path
pq = []
# initialize
dist[S] = 0
heappush(pq, (0, S))
while pq:
    _, u = heappop(pq)
    vstd[u] = True
    for v in link[u]:
        # if vstd[v]:
        #     continue
        for w in link[v]:
            # if vstd[w]:
            #     continue
            for x in link[w]:
                if vstd[x]:
                    continue
                if dist[u] + 1 < dist[x]:
                    dist[x] = dist[u] + 1
                    # prev[v] = u
                    heappush(pq, (dist[x], x))


print(dist[T] if dist[T] != INF else -1)
