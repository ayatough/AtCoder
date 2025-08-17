from itertools import permutations, combinations

N = int(input())
MG = int(input())
EG = [[0] * (N+1) for _ in range(N+1)]
for _ in range(MG):
    u, v = map(int, input().split())
    EG[u][v] = 1

MH = int(input())
EH = [[0] * (N+1) for _ in range(N+1)]
for _ in range(MH):
    u, v = map(int, input().split())
    EH[u][v] = 1

C = {}
for i in range(1,N):
    a = list(map(int, input().split()))
    for j in range(i+1,i+1+len(a)):
        C[(i,j)] = a[j-i-1]

# print(f"{EG=}")
# print(f"{EH=}")
# print(f"{C=}")

INF = 10**13
min_cost = INF
for perm in permutations(range(N)):
    cost = 0
    for u, v in combinations(range(1,N+1), 2):
        gu = perm[u-1] + 1
        gv = perm[v-1] + 1
        gu, gv = min(gu, gv), max(gu, gv)
        if EH[u][v] != EG[gu][gv]:
            cost += C[(u,v)]

    if cost < min_cost:
        min_cost = cost

print(min_cost)
