import sys
N, M = map(int, input().split())
MOD = 10 ** 9 + 7

NG = [False for _ in range(N+1)]
for _ in range(M):
    NG[int(input())] = True

dp = [None for _ in range(N+1)]
dp[0] = 1
dp[1] = 0 if NG[1] else 1
for i in range(2, N+1):
    if NG[i]:
        dp[i] = 0
    else:
        dp[i] = (dp[i-2] + dp[i-1]) % MOD

print(dp[-1])
