from itertools import combinations
from pprint import pprint

N, M = map(int, input().split())
INF = 10**9 * 500 + 1
mat = [[INF] * N for _ in range(N)]
air = [INF] * N

for i in range(N):
    mat[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    mat[a-1][b-1] = mat[b-1][a-1] = c

K, T = map(int, input().split())
if K > 0:
    D = set(map(int, input().split()))
else:
    D = set()

for i in range(N):
    if i+1 in D:
        air[i] = 0

def init(mat, air):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                mat[i][j] = min(min(mat[i][j], mat[i][k] + mat[k][j]), INF)

    for i in range(N):
        for j in range(N):
            air[i] = min(min(air[i], mat[i][j] + air[j]), INF)


def update(mat, air, s, t, cost):
    if mat[s-1][t-1] > cost:
        mat[s-1][t-1] = mat[t-1][s-1] = cost
        for k in [s-1, t-1]:
            for i in range(N):
                for j in range(N):
                    mat[i][j] = min(min(mat[i][j], mat[i][k] + mat[k][j]), INF)

        for i in range(N):
            for j in range(N):
                air[i] = min(min(air[i], mat[i][j] + air[j]), INF)


def update_only_air(mat, air, x):
    if air[x-1] != 0:
        air[x-1] = 0
        for i in range(N):
            for j in range(N):
                air[i] = min(min(air[i], mat[i][j] + air[j]), INF)


def calc(mat, air):
    cost = 0
    for i in range(N):
        for j in range(i+1, N):
            c = min(mat[i][j], air[i] + air[j] + T, INF)
            if c < INF:
                cost += c
    return cost * 2

init(mat, air)

Q = int(input())

cost = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(mat, air, *q[1:])
    elif q[0] == 2:
        update_only_air(mat, air, q[1])
    else:
        cost.append(calc(mat, air))

print(*cost, sep="\n")
