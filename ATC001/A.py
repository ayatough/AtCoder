import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
C = []
sx, sy = 0, 0
for i in range(H):
    c = input()
    if 's' in c:
        sx, sy = c.find('s'), i
    C.append(c)

vstd = [[False for _ in range(W)] for _ in range(H)]
def dfs(i, j):
    if i < 0 or i > H-1 or j < 0 or j > W-1:
        return False
    if vstd[i][j]:
        return False
    if C[i][j] == 'g':
        return True
    vstd[i][j] = True
    if C[i][j] == '#':
        return False
    l = dfs(i,j-1)
    u = dfs(i-1,j)
    r = dfs(i,j+1)
    d = dfs(i+1,j)
    return any([l, u, r, d])

print('Yes' if dfs(sy, sx) else 'No')
