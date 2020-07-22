from copy import deepcopy
H, W = 10, 10
A = []
land = 0
for i in range(H):
    a = input()
    land += a.count('o')
    A.append(a)

def slv():
    for i in range(H):
        for j in range(W):
            if A[i][j] == 'x':
                M = deepcopy(A)
                M[i] = M[i][:j] + 'o' + M[i][j+1:]
                vstd = [[False for _ in range(W)] for _ in range(H)]
                con = dfs(i, j, M, vstd)
                if con == land + 1:
                    return True
    return False

def dfs(i, j, M, vstd):
    if i < 0 or i > H-1 or j < 0 or j > W-1:
        return 0
    if vstd[i][j]:
        return 0
    vstd[i][j] = True
    if M[i][j] == 'x':
        return 0
    l = dfs(i,j-1,M,vstd)
    u = dfs(i-1,j,M,vstd)
    r = dfs(i,j+1,M,vstd)
    d = dfs(i+1,j,M,vstd)
    return 1 + l + u + r + d

print('YES' if slv() else 'NO')
