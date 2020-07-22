import sys
input = sys.stdin.readline
N, T = map(int, input().split())
D = []
for _ in range(N):
    a, b = map(int, input().split())
    D.append((a,-b))

D.sort()

dp = [[0] * (T) for _ in range(N)]
for i in range(1, N):
    a, b = D[i-1]
    b = -b
    for t in range(T):
        dp[i][t] = dp[i-1][t]
        if t >= a:
            dp[i][t] = max(dp[i][t], dp[i-1][t-a]+b)

print(max(-D[i][1] + dp[i][-1] for i in range(1,N)))