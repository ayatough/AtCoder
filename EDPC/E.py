# input
N, M = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[None for __ in range(N*max(V)+1)] for _ in range(N+1)]
dp[0] = [10**9 for _ in range(N*max(V)+1)]
dp[0][0] = 0
for i in range(1, N+1):
    for v in range(N*max(V)+1):
        if V[i-1] >= v:
            dp[i][v] = min(dp[i-1][v], W[i-1])
        else:
            dp[i][v] = min(dp[i-1][v], dp[i-1][v-V[i-1]] + W[i-1])


print(max(i for i, w in enumerate(dp[-1]) if w <= M))
