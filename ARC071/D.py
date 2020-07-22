N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
MOD = 10 ** 9 + 7

xsum, ysum = 0, 0
for i in range(1, N):
    xsum += (X[i] - X[i-1]) * i * (N - i)
    xsum %= MOD
for j in range(1, M):
    ysum += (Y[j] - Y[j-1]) * j * (M - j)
    ysum %= MOD

print((xsum * ysum) % MOD)
