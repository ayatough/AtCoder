K = int(input())
N = 2 ** K
V = [[0 for _ in range(N)] for _ in range(N)]
R = []
for _ in range(N):
    R.append(int(input()))

for i in range(N):
    for j in range(0, i):
        V[i][j] = 1 / (1 + 10 ** ((R[j] - R[i]) / 400))
        V[j][i] = 1 - V[i][j]

dp = [[0 for _ in range(N)] for _ in range(K+1)]
dp[0] = [1] * N

for i in range(1, K+1):
    for j in range(N):
        a = 2 ** (i-1)
        a2 = a * 2
        b = j // a * a
        b2 = j // a2 * a2
        low = b2 + ((b + a) % a2)
        for k in range(low, low+a):
            dp[i][j] += V[j][k] * dp[i-1][k] * dp[i-1][j]

print('\n'.join(map(str, dp[-1])))
