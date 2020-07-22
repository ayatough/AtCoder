N, M = map(int, input().split())
MOD = 10 ** 9 + 7
S = []
for _ in range(M):
    S.append(input())

# N = M case

# dp = [[0, 0, 0] for _ in range(M+1)]
# dp[0] = [1, 0, 0]


# if S[0] == 'Fizz':
#     dp[1][0] += dp[0][0] * 3 + dp[0][1] * 2 + dp[0][2] * 3
# elif S[0] == 'Buzz':
#     dp[1][2] += dp[0][0]
# elif S[0] == 'FizzBuzz':
#     dp[1][0] += 0

# for i in range(2,M+1):
#     if S[i-1] == 'Fizz':
#         dp[i][0] += dp[i-1][0] * 3 + dp[i-1][1] * 2 + dp[i-1][2] * 3
#     elif S[i-1] == 'Buzz':
#         dp[i][0] += 0
#         dp[i][1] += dp[i-1][1] + dp[i-1][2]
#         dp[i][2] += dp[i-1][2] + dp[i-1][0]
#     elif S[i-1] == 'FizzBuzz':
#         dp[i][0] += dp[i-1][0] + dp[i-1][1]
#     dp[i][0] %= MOD
#     dp[i][1] %= MOD
#     dp[i][2] %= MOD

# print(sum(dp[-1]) % MOD)

dp = [[[0, 0, 0] for _ in range(M+1)] for _ in range(N+1)]
dp[0][0] = [1, 0, 0]

dp[1][0][0] += 0
dp[1][0][1] += dp[0][0][0] * 3 + dp[0][0][1] * 3 + dp[0][0][2] * 2
dp[1][0][2] += dp[0][0][0] * 2 + dp[0][0][1] * 3 + dp[0][0][2] * 3

if M > 0:
    if S[0] == 'Fizz':
        dp[1][1][0] += dp[0][0][0] * 3 + dp[0][0][1] * 2 + dp[0][0][2] * 3
    elif S[0] == 'Buzz':
        dp[1][1][2] += dp[0][0][0]
    elif S[0] == 'FizzBuzz':
        dp[1][1][0] += 0

for i in range(2, N+1):
    if i <= N-M:
        dp[i][0][0] += 0
        dp[i][0][1] += dp[i-1][0][0] * 3 + dp[i-1][0][1] * 3 + dp[i-1][0][2] * 2
        dp[i][0][2] += dp[i-1][0][0] * 2 + dp[i-1][0][1] * 3 + dp[i-1][0][2] * 3

    dp[i][0][0] %= MOD
    dp[i][0][1] %= MOD
    dp[i][0][2] %= MOD

    for j in range(max(1, i-N+M), min(i+1, M+1)):
        dp[i][j][0] += 0
        dp[i][j][1] += dp[i-1][j][0] * 3 + dp[i-1][j][1] * 3 + dp[i-1][j][2] * 2
        dp[i][j][2] += dp[i-1][j][0] * 2 + dp[i-1][j][1] * 3 + dp[i-1][j][2] * 3
        if S[j-1] == 'Fizz':
            dp[i][j][0] += dp[i-1][j-1][0] * 3 + dp[i-1][j-1][1] * 2 + dp[i-1][j-1][2] * 3
        elif S[j-1] == 'Buzz':
            dp[i][j][0] += 0
            dp[i][j][1] += dp[i-1][j-1][1] + dp[i-1][j-1][2]
            dp[i][j][2] += dp[i-1][j-1][2] + dp[i-1][j-1][0]
        elif S[j-1] == 'FizzBuzz':
            dp[i][j][0] += dp[i-1][j-1][0] + dp[i-1][j-1][1]
        dp[i][j][0] %= MOD
        dp[i][j][1] %= MOD
        dp[i][j][2] %= MOD

print(sum(dp[-1][-1]) % MOD)
