N, K = map(int, input().split())
A = list(map(int, input().split()))

cum = [0]
piv = 0
dp = [0 for _ in range(N+1)]
dp[0] = 0
for i in range(N):
    cum.append(cum[-1] + A[i])
    if cum[-1] < K:
        continue
    dp[i+1] = dp[i]
    while cum[-1] - cum[piv] >= K:
        piv += 1
        dp[i+1] += 1

print(sum(dp))
