N = input()
L = len(N)

dp = [[[[0] * 2 for _ in range(2)] for _ in range(2)] for _ in range(2)]
pp = [[[[0] * 2 for _ in range(2)] for _ in range(2)] for _ in range(2)]
dp[0][0][0][0] = 1

for i in range(L):
    pp, dp = dp, pp
    dp = [[[[0] * 2 for _ in range(2)] for _ in range(2)] for _ in range(2)]
    n = int(N[i])
    dp[0][0][0][1] += pp[0][0][0][1]
    dp[1][0][0][1] += pp[0][0][0][1] + pp[1][0][0][1]
    dp[0][1][0][1] += pp[0][0][0][1] + pp[0][1][0][1]
    dp[0][0][1][1] += pp[0][0][0][1] + pp[0][0][1][1]
    dp[1][1][0][1] += pp[1][0][0][1] + pp[0][1][0][1] + pp[1][1][0][1] * 2
    dp[1][0][1][1] += pp[1][0][0][1] + pp[0][0][1][1] + pp[1][0][1][1] * 2
    dp[0][1][1][1] += pp[0][1][0][1] + pp[0][0][1][1] + pp[0][1][1][1] * 2
    dp[1][1][1][1] += pp[1][1][0][1] + pp[1][0][1][1] + pp[0][1][1][1] + pp[1][1][1][1] * 3
    if n > 0:
        dp[0][0][0][1] += pp[0][0][0][0]
    if n > 3:
        dp[1][0][0][1] += pp[1][0][0][0] + pp[0][0][0][0]
        dp[1][1][0][1] += pp[1][1][0][0] + pp[0][1][0][0]
        dp[1][0][1][1] += pp[1][0][1][0] + pp[0][0][1][0]
        dp[1][1][1][1] += pp[1][1][1][0] + pp[0][1][1][0]
    if n > 5:
        dp[0][1][0][1] += pp[0][1][0][0] + pp[0][0][0][0]
        dp[1][1][0][1] += pp[1][1][0][0] + pp[1][0][0][0]
        dp[0][1][1][1] += pp[0][1][1][0] + pp[0][0][1][0]
        dp[1][1][1][1] += pp[1][1][1][0] + pp[1][0][1][0]
    if n > 7:
        dp[0][0][1][1] += pp[0][0][1][0] + pp[0][0][0][0]
        dp[1][0][1][1] += pp[1][0][1][0] + pp[1][0][0][0]
        dp[0][1][1][1] += pp[0][1][1][0] + pp[0][1][0][0]
        dp[1][1][1][1] += pp[1][1][1][0] + pp[1][1][0][0]
    if n == 0:
        dp[0][0][0][0] += pp[0][0][0][0]
    if n == 3:
        dp[1][0][0][0] += pp[1][0][0][0] + pp[0][0][0][0]
        dp[1][1][0][0] += pp[1][1][0][0] + pp[0][1][0][0]
        dp[1][0][1][0] += pp[1][0][1][0] + pp[0][0][1][0]
        dp[1][1][1][0] += pp[1][1][1][0] + pp[0][1][1][0]
    if n == 5:
        dp[0][1][0][0] += pp[0][1][0][0] + pp[0][0][0][0]
        dp[1][1][0][0] += pp[1][1][0][0] + pp[1][0][0][0]
        dp[0][1][1][0] += pp[0][1][1][0] + pp[0][0][1][0]
        dp[1][1][1][0] += pp[1][1][1][0] + pp[1][0][1][0]
    if n == 7:
        dp[0][0][1][0] += pp[0][0][1][0] + pp[0][0][0][0]
        dp[1][0][1][0] += pp[1][0][1][0] + pp[1][0][0][0]
        dp[0][1][1][0] += pp[0][1][1][0] + pp[0][1][0][0]
        dp[1][1][1][0] += pp[1][1][1][0] + pp[1][1][0][0]


print(sum(dp[1][1][1]))