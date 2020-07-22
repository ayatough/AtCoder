N, K = map(int, input().split())
MOD = 10 ** 9 + 7

dp = [[0, 0] for _ in range(N+1)]
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2,N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i][0] - (0 if i < K else dp[i-K][0])
    dp[i][0] %= MOD
    dp[i][1] %= MOD

print(dp[-1][1])
