H, W = map(int, input().split())
MOD = 10 ** 9 + 7
A = ['#' * (W+1)]
for _ in range(H):
    A.append('#' + input())

dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
dp[0][1] = 1

for y in range(1,H+1):
    for x in range(1,W+1):
        if A[y][x] == '#':
            dp[y][x] = 0
        else:
            dp[y][x] = dp[y-1][x] + dp[y][x-1]
            dp[y][x] %= MOD

print(dp[-1][-1])
