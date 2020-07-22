import sys
input = sys.stdin.readline
N, T = map(int, input().split())
D = []
for _ in range(N):
    a, b = map(int, input().split())
    D.append((a,-b))

D.sort()

dp = [[0] * T for _ in range(N+1)]
pa = [0] * T  # prev a
for i in range(1, N+1):
    a, b = D[i-1]
    b = -b
    for t in range(T):
        if pa[t] <= t:
            upd = dp[i-1][t-pa[t]]+b
            if upd > dp[i-1][t]:
                dp[i][t] = upd
                pa[t] = a
            else:
                dp[i][t] = dp[i-1][t]
        else:
            if b > dp[i-1][t]:
                dp[i][t] = b
                pa[t] = a
            else:
                dp[i][t] = dp[i-1][t]

print(dp[-1][-1])