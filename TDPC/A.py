N = int(input())
P = list(map(int, input().split()))
MAX = 10 ** 4
dp = [False for _ in range(MAX+1)]
dp[0] = True
for i in range(N):
    for n in range(MAX-P[i],-1,-1):
        if dp[n]:
            dp[n+P[i]] = True

print(dp.count(True))
