# input
N = int(input())
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7

dp = [[None for _ in range(N)] for __ in range(N+1)]
dp[0] = [0 for _ in range(N)]

def xors(i, j):
    xor = A[i-1]
    for k in range(i,j):
        xor ^= A[k]
    return xor


for i in range(1, N+1):
    dp[i][0] = 1
    for j in range(1,i):
        dp[i][j] = 0
        for k in range(j):
            if xors(k+1, j) == xors(j+1, i):
                dp[i][j] += dp[j][k]

print(sum(dp[-1]) % MOD)
