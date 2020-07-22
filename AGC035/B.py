from collections import deque
N, M = map(int, input().split())
V = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

def zen(V):
    W = []
    q = deque()
    q.append(1)
    vstd = {i: 0 for i in range(1,N+1)}

    while q:
        u = q.popleft()
        if vstd[u]:
            continue
        vstd[u] = True
        W.append(u)
        for v in V[u]:
            if vstd[v]:
                continue
            q.append(v)
    return W

if M % 2 != 0:
    print(-1)
else:

    U = zen(V)
    W = {i: [] for i in range(1,N+1)}

    for u in U[::-1]:
        for v in V[u]:
            if v in W[u] or u in W[v]:
                continue
            if len(W[u]) % 2 == 0:
                W[v].append(u)
            else:
                W[u].append(v)

    for w in W:
        for v in W[w]:
            print(w, v)
