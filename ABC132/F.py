from collections import deque
N, K = map(int, input().split())
MOD = 10 ** 9 + 7

# guchoku case

# dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

# for i in range(N+1):
#     dp[1][i] = 1
# for i in range(K):
#     for j in range(1,N+1):
#         for k in range(1, N // j + 1):
#             dp[i+1][j] += dp[i][k]
#             dp[i+1][j] %= MOD

JN = deque()  # N//j table
SQN = int(N**0.5)
JN.append(SQN)

if SQN**2 != N:
    JN.append(N//SQN)
for j in range(SQN-1, 0, -1):
    JN.appendleft(j)
    JN.append(N//j)
JN.appendleft(0)

# JN.sort()
# PJN = {JN[i]: JN[i-1] for i in range(1, len(JN))}  # prev jn
LJN = len(JN)

dp = [[0 for _ in range(LJN)] for _ in range(K)]
cdp = [[0 for _ in range(LJN)] for _ in range(K)]
w = [0 for _ in range(LJN)]

# init dp
prv = 0
for i in range(1,LJN):
    jn = JN[i]
    dp[0][i] = 1
    w[i] = jn - prv
    cdp[0][i] = jn
    prv = JN[i]

for i in range(K-1):
    for j in range(1,LJN):
        dp[i+1][j] = cdp[i][LJN-j]
        dp[i+1][j] %= MOD
        cdp[i+1][j] = cdp[i+1][j-1] + dp[i+1][j] * w[j]
        cdp[i+1][j] %= MOD

print(cdp[-1][-1])
