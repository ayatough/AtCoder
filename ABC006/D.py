from bisect import bisect_left
N = int(input())
C = list(int(input()) for _ in range(N))
INF = 10 ** 5
dp = [INF]
for c in C:
    if c > dp[-1]:
        dp.append(c)
    else:
        i = bisect_left(dp, c)
        dp[i] = c

print(N - len(dp))
