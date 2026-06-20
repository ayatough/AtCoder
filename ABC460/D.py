H, W = map(int, input().split())
S = []
num_black = 0
for _ in range(H):
    S.append(input().strip())
    for s in S[-1]:
        if s == "#":
            num_black += 1

degenerated = False
if num_black == H*W or num_black == 0:
    degenerated = True

# Equilibrium
E = []

if not degenerated:

    # distance_map black and white
    INF = 10**7 - 1
    Db = [[INF] * (W+2) for _ in range(H+2)]
    Dw = [[INF] * (W+2) for _ in range(H+2)]

    for D, m in zip([Db, Dw], ".#"):

        for y in range(1, H+1):
            for x in range(1, W+1):
                if S[y-1][x-1] == m:
                    D[y][x] = 0
                else:
                    D[y][x] = min(D[y][x], D[y-1][x-1] + 1, D[y][x-1] + 1, D[y-1][x] + 1)

        for y in range(1, H+1):
            for x in range(W, 0, -1):
                if S[y-1][x-1] == m:
                    D[y][x] = 0
                else:
                    D[y][x] = min(D[y][x], D[y-1][x+1] + 1, D[y][x+1] + 1, D[y-1][x] + 1)

        for y in range(H, 0, -1):
            for x in range(W, 0, -1):
                if S[y-1][x-1] == m:
                    D[y][x] = 0
                else:
                    D[y][x] = min(D[y][x], D[y+1][x+1] + 1, D[y][x+1] + 1, D[y+1][x] + 1)

        for y in range(H, 0, -1):
            for x in range(1, W+1):
                if S[y-1][x-1] == m:
                    D[y][x] = 0
                else:
                    D[y][x] = min(D[y][x], D[y+1][x-1] + 1, D[y][x-1] + 1, D[y+1][x] + 1)

    for db_, dw_ in zip(Db[1:-1], Dw[1:-1]):
        db = db_[1:-1]
        dw = dw_[1:-1]
        E.append("".join([("#" if max(b-1, w)%2 == 0 else ".") for (b, w) in zip(db, dw)]))

else:
    for _ in range(H):
        E.append("." * W)

print(*E, sep="\n")

# print(*S, sep="\n")
# print("="*20)

# for i in range(10):
#     newS = []
#     for j in range(H):
#         row = ""
#         for k in range(W):
#             s = S[j][k]
#             if s == "#":
#                 n = "."
#             else:
#                 lt = S[max(0, j-1)][max(0, k-1)]
#                 t = S[max(0, j-1)][k]
#                 rt = S[max(0, j-1)][min(W-1, k+1)]
#                 l = S[j][max(0, k-1)]
#                 r = S[j][min(W-1, k+1)]
#                 lb = S[min(H-1, j+1)][max(0, k-1)]
#                 b = S[min(H-1, j+1)][k]
#                 rb = S[min(H-1, j+1)][min(W-1, k+1)]
#                 if lt == "#" or t == "#" or rt == "#" or l == "#" or r == "#" or lb == "#" or b == "#" or rb == "#":
#                     n = "#"
#                 else:
#                     n = "."
#             row += n
#         newS.append(row)
#     S = newS
#     print(*S, sep="\n")
#     print("="*20)
