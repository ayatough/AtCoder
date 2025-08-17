N, K = map(int, input().split())
M = 998244353
A = list(map(int, input().split()))

C = [0]
for a in A:
    C.append(C[-1] + a)


# O(N^2)
# dp = [0] * (N+1)
# dp[0] = 1
# for i in range(1,N+1):
#     for j in range(i):
#         if C[i] - C[j] != K:
#             dp[i] += dp[j]
#             dp[i] %= M
# print(dp[-1])

dp = None
memo = {0: 1}
dpsum = 1
for i in range(1,N+1):
    dp = dpsum - memo.get(C[i] - K, 0)
    dp %= M
    dpsum += dp
    dpsum %= M
    memo[C[i]] = memo.get(C[i], 0) + dp
    memo[C[i]] %= M

print(dp)
