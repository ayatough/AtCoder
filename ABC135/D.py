S = input()
N = len(S)
MOD = 10 ** 9 + 7

dp = [0 for _ in range(13)]
pp = [0 for _ in range(13)]

dp[0] = 1
for i in range(N):
    pp, dp = dp, pp
    for d in range(13):
        dp[d] = 0
    s = S[N-i-1]
    b = pow(10, i, 13)
    if s == '?':
        for d in range(13):
            for e in range(10):
                dp[(d+b*e)%13] += pp[d]
                dp[(d+b*e)%13] %= MOD
    else:
        s = int(s)
        for d in range(13):
            dp[(d+b*s)%13] += pp[d]
            dp[(d+b*s)%13] %= MOD

print(dp[5])
