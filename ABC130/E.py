N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
MOD = 10 ** 9 + 7

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
dp[0] = [0 for _ in range(N+1)]

for i in range(1,M+1):
    for j in range(N+1):
        if j == 0:
            dp[i][j] = 0
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        if S[j-1] == T[i-1]:
            dp[i][j] += dp[i-1][j-1] + 1
        dp[i][j] %= MOD
        

print((dp[-1][-1] + 1) % MOD)
