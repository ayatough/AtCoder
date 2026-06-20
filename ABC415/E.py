from pprint import pprint
H, W = map(int, input().split())
A = []

for _ in range(H):
    A.append(list(map(int, input().split())))

P = list(map(int, input().split()))

D = [[0] * (W+1) for _ in range(H+1)]
E = [[0] * (W+1) for _ in range(H+1)]
for y in range(H):
    for x in range(W):
        # A[y][x] -= P[x + y]
        # D[y+1][x+1] = -A[y][x] + min(D[y][x+1], E[y+1][x])
        print(x, y, D[y][x+1] + A[y][x] - P[x + y])
        if D[y][x+1] + A[y][x] - P[x + y] < 0:
            print("A")
            D[y+1][x+1] = max(D[y+1][x+1], D[y][x+1] + A[y][x] - P[x + y])
        else:
            D[y+1][x+1] = max(D[y+1][x+1], D[y][x+1] + A[y][x] - P[x + y])

        print(x, y, D[y+1][x] + A[y][x] - P[x + y])
        if D[y+1][x] + A[y][x] - P[x + y] < 0:
            print("B")
            D[y+1][x+1] = max(D[y+1][x+1], D[y][x+1] + A[y][x] - P[x + y])
        else:
            D[y+1][x+1] = max(D[y+1][x+1], D[y+1][x] + A[y][x] - P[x + y])
        # E[y+1][x+1] = max(D[y+1][x+1], E[y][x+1], E[y+1][x])

pprint(A)
pprint(D)
# pprint(E)
