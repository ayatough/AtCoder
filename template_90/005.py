import sys
input = sys.stdin.readline

N, B, K = map(int, input().split())
C = list(map(int, input().split()))
MOD = 10**9 + 7

DP = [[0] * B for _ in range(N+1)]
DP[0][0] = 1

for i in range(N):
    CD = [-1] * 10
    d = pow(10, i, B)
    for c in C:
        CD[c] = (d * c) % B
    for b in range(B):
        for c in C:
            d = CD[c]
            m = (b+d)%B
            DP[i+1][m] = (DP[i+1][m] + DP[i][b]) % MOD

print(DP[-1][0])
