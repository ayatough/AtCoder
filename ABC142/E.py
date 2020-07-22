import sys
input = sys.stdin.readline
N, M = map(int, input().split())
INF = 10 ** 12
dp = [INF] * (2**N)
dp[0] = 0
for i in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    base = sum(2**(c-1) for c in C)
    for j in range(2**N):
        if any(not ((j >> (c-1)) & 1) for c in C):
            step = base - sum(2**(c-1) for c in C if ((j >> (c-1)) & 1))
            dp[j+step] = min(dp[j+step], dp[j]+a)

print(dp[-1] if dp[-1] < INF else -1)
