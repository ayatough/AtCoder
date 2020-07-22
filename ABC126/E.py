from collections import deque
N, M = map(int, input().split())
X, Y = [], []

# union-find
class UF(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def root(self, v):
        if v == self.parent[v]:
            return v
        else:
            self.parent[v] = self.root(self.parent[v])
            return self.parent[v]
    
    def unite(self, u, v):
        u, v = self.root(u), self.root(v)
        if (u == v):
            return
        self.parent[u] = v

uf = UF(N)
# vertex table
V = [[] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    uf.unite(x-1, y-1)
    V[x-1].append(y-1)
    V[y-1].append(x-1)

# search connection
visit = [False for _ in range(N)]

def dfs(v, V, visit):
    search = deque()
    # search = []
    visit[v] = True
    search.append(v)
    while len(search) > 0:
        v = search.pop()
        for u in V[v]:
            if not visit[u]:
                visit[u] = True
                search.append(u)
    return visit

con = 0
# while not all(visit):
#     v = visit.index(False)
#     if V[v] != []:
#         visit = dfs(v, V, visit)
#     else:
#         visit[v] = True
#     con += 1

print(len(set(uf.root(x) for x in range(N))))

# print(con)


