from collections import deque
N = int(input())
V = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    a, b, c = map(int, input().split())
    V[a].append((b, c))
    V[b].append((a, c))
nq, k = map(int, input().split())
Q = []
for _ in range(nq):
    x, y = map(int, input().split())
    Q.append((x, y))

dist = {i: 0 for i in range(1, N+1)}
dq = deque()
dq.append(k)
dist[k] = 0
vstd = {i: False for i in range(1, N+1)}
while len(dq) > 0:
    u = dq.popleft()
    vstd[u] = True
    for vw in V[u]:
        v, w = vw
        if vstd[v]:
            continue
        dq.append(v)
        dist[v] = dist[u] + w

for q in Q:
    x, y = q
    print(dist[x] + dist[y])
