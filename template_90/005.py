import sys
input = sys.stdin.readline
from copy import copy

N, B, K = map(int, input().split())
C = list(map(int, input().split()))
MOD = 10**9 + 7

L = N.bit_length()
A = [[[0] * B for _ in range(B)]]

for i in range(B):
    for c in C:
        m = (10*i + c) % B
        A[0][i][m] += 1

for _ in range(L):
    cum = [[0] * B for _ in range(B)]
    for i in range(B):
        for j in range(B):
            for k in range(B):
                cum[i][j] += A[-1][i][k] * A[-1][k][j]
                cum[i][j] %= MOD
    A.append(cum)

DP = [0] * B
DP[0] = 1
for i, bit in enumerate(bin(N)[2:][::-1]):
    PP = [0] * B
    if bit == "0":
        continue
    for j in range(B):
        for k in range(B):
            PP[j] += A[i][j][k] * DP[k]
            PP[j] %= MOD
    DP = copy(PP)

print(DP[0])
