# input
N, M = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[None for __ in range(M+1)] for _ in range(N+1)]
dp[0] = [0 for _ in range(M+1)]
for i in range(1, N+1):
    for w in range(M+1):
        if W[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-W[i-1]] + V[i-1])
        else:
            dp[i][w] = dp[i-1][w]


print(max(dp[-1]))
