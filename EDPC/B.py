# input
N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [None for _ in range(N)]
# initiate
dp[0] = 0

for i in range(1, N):
    min_ = min(dp[k] + abs(H[k]-H[i]) for k in range(max(0, i-K), i))
    dp[i] = min_

print(dp[-1])
pass