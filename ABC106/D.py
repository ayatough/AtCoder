N, M, Q = map(int, input().split())
dp = [[0] * N for _ in range(N)]
for _ in range(M):
    l, r = map(int, input().split())
    dp[r-1][l-1] += 1

for i in range(1,N):
    for j in range(N-i):
        l, r = j, j+i
        dp[r][l] += dp[r-1][l] + dp[r][l+1] - dp[r-1][l+1]


for _ in range(Q):
    p, q = map(int, input().split())
    print(dp[q-1][p-1])
