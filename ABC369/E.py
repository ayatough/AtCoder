from itertools import permutations, product

N, M = map(int, input().split())
INF = 10**15
Adj = [[INF] * (N+1) for _ in range(N+1)]
Brd = [(0, 0, 0)]

for i in range(1, N+1):
    Adj[i][i] = 0

for _ in range(M):
    u, v, t = map(int, input().split())
    Adj[u][v] = Adj[v][u] = min(Adj[u][v], t)
    Brd.append((u, v, t))

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            new = Adj[i][k] + Adj[k][j]
            if Adj[i][j] > new:
                Adj[i][j] = Adj[j][i] = new

Q = int(input())
ans = []

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    dist = INF
    base = sum(Brd[b][2] for b in B)
    for bs in permutations(B):
        for inv in product(range(2), repeat=K):
            cur = Adj[1][Brd[bs[0]][inv[0]]] + Adj[Brd[bs[-1]][1-inv[-1]]][N]
            for k in range(K-1):
                cur += Adj[Brd[bs[k]][1-inv[k]]][Brd[bs[k+1]][inv[k+1]]]
            dist = min(dist, cur)
    ans.append(dist + base)

print(*ans, sep="\n")
