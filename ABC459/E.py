import sys

MOD = 998244353
N = int(input())
intm = lambda x: int(x) - 1
parents = [-1] + list(map(intm, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
MAXD = max(D)

sys.setrecursionlimit(10*N)

childs = [[] for _ in range(N)]
for c, p in enumerate(parents):
    if p < 0:
        continue
    childs[p].append(c)

visited = [False] * N

combinations = []
def dfs(v):
    visited[v] = True
    is_leaf = (len(childs[v]) == 0)
    if is_leaf:
        r = C[v] - D[v]
        combinations.append((C[v], D[v]))
        return r

    # accum = 1
    remains = C[v]
    for c in childs[v]:
        if visited[c]:
            continue
        r = dfs(c)
        remains += r

    combinations.append((remains, D[v]))

    return remains - D[v]

dfs(0)

inv = [0] + [pow(i, MOD-2, MOD) for i in range(1, MAXD + 1)]

ans = 1
for comb in combinations:
    if comb[1] == 1:
        ans = (ans * comb[0]) % MOD
    else:
        for i in range(comb[1]):
            ans = (ans * (comb[0] - i)) % MOD
            ans = (ans * inv[comb[1] - i]) % MOD

print(ans)
