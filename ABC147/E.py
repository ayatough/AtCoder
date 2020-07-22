import sys
input = sys.stdin.readline
H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))
B = []
C = []
for y in range(H):
    B.append(list(map(int, input().split())))
    C.append(list(abs(a-b) for (a, b) in zip(A[y], B[y])))
VMAX = 80*159+1
dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] |= 1 << C[0][0]
for y in range(H):
    for x in range(W):
        if y==0 and x==0:
            continue
        if y-1 >= 0:
            dp[y][x] |= dp[y-1][x] << C[y][x]
            dp[y][x] |= dp[y-1][x] >> C[y][x]
            d = C[y][x]+1
            r = format(dp[y-1][x] & (2**d-1), '0'+str(d)+'b')
            r = r[::-1]
            dp[y][x] |= int(r, 2)
        if x-1 >= 0:
            dp[y][x] |= dp[y][x-1] << C[y][x]
            dp[y][x] |= dp[y][x-1] >> C[y][x]
            d = C[y][x]+1
            r = format(dp[y][x-1] & (2**d-1), '0'+str(d)+'b')
            r = r[::-1]
            dp[y][x] |= int(r, 2)
ans = -1
for v in range(VMAX):
    if dp[-1][-1] >> v & 1:
        ans = v
        break
print(ans)