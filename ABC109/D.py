H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

actions = []
paths = []
for y in range(H):
    for x in range(W):
        if y%2 == 0:
            paths.append((y, x))
        else:
            paths.append((y, W-x-1))

for i in range(H*W-1):
    y, x = paths[i]
    if A[y][x]%2 == 1:
        actions.append((paths[i][0]+1, paths[i][1]+1, paths[i+1][0]+1, paths[i+1][1]+1))
        ny, nx = paths[i+1]
        A[ny][nx] += 1

print(len(actions))
for a in actions:
    print(*a)
