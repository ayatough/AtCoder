N = int(input())
S = input()

dp = [[0] * N for _ in range(N)]

dp[-1] = [1 if s == S[-1] else 0 for s in S]
for i in range(N-2, -1, -1):
    dp[i][-1] = 1 if S[i] == S[-1] else 0
    for j in range(N-2, -1, -1):
        if S[i] == S[j]:
            dp[i][j] = dp[i+1][j+1] + 1

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if dp[i][j] > 0:
            ans = max(ans, min(dp[i][j], j-i))

print(ans)
