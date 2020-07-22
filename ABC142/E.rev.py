# bitDP
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
INF = 10 ** 12
T = [2**i for i in range(N)]
dp = [INF] * (2**N)
dp[0] = 0
for i in range(M):
    a, b = map(int, input().split())
    C = list(map(int, input().split()))
    step = sum(T[c-1] for c in C)
    for j in range(2**N):
        dp[step|j] = min(dp[step|j], dp[j]+a)

print(dp[-1] if dp[-1] < INF else -1)
