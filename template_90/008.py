import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()
MOD = 10**9 + 7

atcoder = "atcoder"
DP = [[0] * (len(atcoder)+1) for _ in range(N+1)]
DP[0][0] = 1

for i in range(1, N+1):
    s = S[i-1]
    DP[i][0] = DP[i-1][0]
    for j_, a in enumerate(atcoder):
        j = j_ + 1
        DP[i][j] = DP[i-1][j]
        if s == a:
            DP[i][j] += DP[i-1][j-1]
            DP[i][j] %= MOD

print(DP[-1][-1])
