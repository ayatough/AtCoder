L = input()
MOD = 10 ** 9 + 7

N = len(L)
dp = [[None, None] for _ in range(N+1)]
SMALL, POSBL = 1, 0
dp[0][POSBL] = 1
dp[0][SMALL] = 0

for i in range(1, N+1):
    pp, ps, ss = (2, 1, 3) if L[i-1] == '1' else (1, 0, 3)
    dp[i][POSBL] = (dp[i-1][POSBL] * pp) % MOD
    dp[i][SMALL] = (dp[i-1][SMALL] * ss + dp[i-1][POSBL] * ps) % MOD

print(sum(dp[-1]) % MOD)
