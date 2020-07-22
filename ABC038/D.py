from bisect import bisect_left
N = int(input())
B = []
for _ in range(N):
    w, h = map(int, input().split())
    B.append((h, -w))
INF = 10 ** 5 + 1
dp = [INF]
B.sort()
for b in B:
    if -b[1] > dp[-1]:
        dp.append(-b[1])
    else:
        i = bisect_left(dp, -b[1])
        dp[i] = -b[1]

print(len(dp))
