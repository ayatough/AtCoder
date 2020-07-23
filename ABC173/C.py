from itertools import product

H, W, K = map(int, input().split())
ary = []
for y in range(H):
    ary.append(input())

case = 0
for yb in range(1<<H):
    for xb in range(1<<W):
        nb = 0
        for y in range(H):
            for x in range(W):
                if ((not ((yb >> y) & 1) and ((xb >> x) & 1))) and ary[y][x] == '#':
                    nb += 1
        if nb == K:
            case += 1

print(case)
