from math import atan2, sqrt
N = int(input())
E = []
for _ in range(N):
    x, y = map(int, input().split())
    d = atan2(y, x)
    E.append((d, x, y))

E.sort()

dp = [[(0, 0)] * N for _ in range(N)]

ans = 0
for i in range(N):
    _, xi, yi = E[i]
    dist = xi ** 2 + yi ** 2
    ans = max(ans, dist)
    dp[i][i] = (xi, yi)
    for j in range(i+1,i+N):
        j %= N
        _, xj, yj = E[j]
        dp[i][j] = (dp[i][j-1][0] + xj, dp[i][j-1][1] + yj)
        dist = dp[i][j][0] ** 2 + dp[i][j][1] ** 2
        ans = max(ans, dist)

print(sqrt(ans))
