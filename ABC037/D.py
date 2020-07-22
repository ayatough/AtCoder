import sys
sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

dp = [[0 for _ in range(W)] for _ in range(H)]
cum = 0

def dfs(i, j):
    if dp[i][j] > 0:
        return dp[i][j]
    a = 1
    for di, dj in D :
        i_, j_ = i+di, j+dj
        if 0 <= i_ < H and 0 <= j_ < W and A[i][j] < A[i_][j_] :
            a += dfs(i_, j_)
            a %= MOD

    # if i > 0 and A[i][j] < A[i-1][j]:
    #     a += dfs(i-1, j)
    #     a %= MOD
    # if j > 0 and A[i][j] < A[i][j-1]:
    #     a += dfs(i, j-1)
    #     a %= MOD
    # if i < H-1 and A[i][j] < A[i+1][j]:
    #     a += dfs(i+1, j)
    #     a %= MOD
    # if j < W-1 and A[i][j] < A[i][j+1]:
    #     a += dfs(i, j+1)
    #     a %= MOD
    dp[i][j] = a
    return a

for i in range(H):
    for j in range(W):
        cum += dfs(i, j)
        cum %= MOD

print(cum)
