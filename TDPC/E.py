D = int(input())
N = input()
MOD = 10 ** 9 + 7

dp = [[[0, 0] for _ in range(D)] for _ in range(len(N)+1)]
dp[0][0][0] = 1

for i in range(len(N)):
    n = int(N[i])
    for d in range(D):
        dp[i+1][(d+n)%D][0] += dp[i][d][0]
        for e in range(10):
            if e < n:
                dp[i+1][(d+e)%D][1] += dp[i][d][0]
            dp[i+1][(d+e)%D][1] += dp[i][d][1]
            dp[i+1][(d+e)%D][1] %= MOD

print((sum(dp[-1][0]) - 1) %MOD)
