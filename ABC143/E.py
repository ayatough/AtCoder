import sys
input = sys.stdin.readline
N, M, L = map(int, input().split())
INF = float('inf')
VD = [[INF] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    VD[a][b] = c
    VD[b][a] = c
for i in range(N):
    VD[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if VD[i][j] > VD[i][k] + VD[k][j]:
                VD[i][j] = VD[i][k] + VD[k][j]

WD = [[INF] * N for _ in range(N)]
for i in range(N):
    WD[i][i] = 0
    for j in range(i+1,N):
        d = VD[i][j]
        if d <= L:
            WD[i][j] = 1
            WD[j][i] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if WD[i][j] > WD[i][k] + WD[k][j]:
                WD[i][j] = WD[i][k] + WD[k][j]

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    print(WD[s-1][t-1]-1 if WD[s-1][t-1] < INF else -1)
