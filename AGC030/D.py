# input
N, Q = map(int, input().split())
A = [int(input()) for _ in range(N)]
XY = []
for _ in range(Q):
    XY.append(tuple(map(int, input().split())))

dp = [[[None for _ in range(N)] for __ in range(N)] for ___ in range(Q+1)]
for i in range(N):
    for j in range(N):
        # inverse case
        dp[0][i][j] = 1 if A[i] > A[j] else 0


def get_past_value(dp, cur, i, j):
    past = 1
    while True:
        xprev = dp[cur-past][i][j]
        if xprev is not None:
            xprev *= pow(2, past-1)
            return xprev
        past += 1


for t in range(1, Q+1):
    x, y = tuple(b-1 for b in XY[t-1])

    # dp[t] = [[v * 2 for v in r] for r in dp[t-1]]

    for j in range(N):
        if j != x and j != y:
            dpx, dpy = (get_past_value(dp, t, xy, j) for xy in (x, y))
            dp[t][x][j] = dp[t][y][j] = dpx + dpy
            # dp[t][x][j] = dp[t-1][x][j] + dp[t-1][y][j]
            # dp[t][y][j] = dp[t-1][y][j] + dp[t-1][x][j]

    for i in range(N):
        if i != x and i != y:
            dpx, dpy = (get_past_value(dp, t, i, xy) for xy in (x, y))
            dp[t][i][x] = dp[t][i][y] = dpx + dpy
            # dp[t][i][x] = dp[t-1][i][x] + dp[t-1][i][y]
            # dp[t][i][y] = dp[t-1][i][y] + dp[t-1][i][x]

    dpx, dpy = (get_past_value(dp, t, a, b) for (a, b) in zip((x, y), (y, x)))
    dp[t][x][y] = dp[t][y][x] = dpx + dpy
    # dp[t][x][y] = dp[t-1][x][y] + dp[t-1][y][x]
    # dp[t][y][x] = dp[t-1][y][x] + dp[t-1][x][y]

    # for i in range(N):
    #     for j in range(N):
    #         dp[t][i][j] = dp[t-1][i][j] * 2
    #         if i == j:
    #             dp[t][i][j] = 0
    #             continue
    #         if i in xy and j in xy:
    #             dp[t][i][j] = dp[t-1][i][j] + dp[t-1][j][i]
    #             continue
    #         if i in xy and j not in xy:
    #             a = xy[0] if xy[1] == i else xy[1]
    #             dp[t][i][j] = dp[t-1][i][j] + dp[t-1][a][j]
    #             continue
    #         if i not in xy and j in xy:
    #             a = xy[0] if xy[1] == j else xy[1]
    #             dp[t][i][j] = dp[t-1][i][j] + dp[t-1][i][a]
    #             continue

res = 0
for i, r in enumerate(dp[-1]):
    for j, v in enumerate(r[i+1:]):
        tmp = 0
        if v is not None:
            tmp = v
            # res += v
        else:
            tmp = get_past_value(dp, -1, i, i+j+1) * 2
            # res += get_past_value(dp, -1, i, j) * 2
        res += tmp

print(res)

# print(sum(v for i, r in enumerate(dp[-1]) for v in r[i+1:]))

# dp = [[[] for __ in range(N)] for ___ in range(N)]
# for i in range(N):
#     for j in range(N):
#         # inverse case
#         dp[i][j].append(1 if A[i] > A[j] else 0)

# for t in range(1, Q+1):
#     x, y = tuple(b-1 for b in XY[t-1])
#     for j in range(N):
#         if j != x and j != y:
#             dp[x][j].append(dp[x][j][-1] + dp[y][j][-1])
#             dp[y][j].append(dp[y][j][-1] + dp[x][j][-1])

#     for i in range(N):
#         if i != x and i != y:
#             dp[i][x].append(dp[i][x][-1] + dp[i][y][-1])
#             dp[i][y].append(dp[i][y][-1] + dp[i][x][-1])

#     dp[x][y].append(dp[x][y][-1] + dp[y][x][-1])
#     dp[y][x].append(dp[y][x][-1] + dp[x][y][-1])

# print(sum(v[-1] for i, r in enumerate(dp) for v in r[i+1:]))
