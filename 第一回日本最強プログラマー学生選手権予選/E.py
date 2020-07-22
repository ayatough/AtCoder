import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N, H, W = map(int, input().split())
RCA = []

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

for _ in range(N):
    r, c, a = map(int, input().split())
    r, c = r-1, c-1
    RCA.append((a, r, c))

RCA.sort(reverse=True)
RCA = deque(RCA)

uf = UF(H+W+1)  # r0, r1, ..., rH, c0, c1, ..., cW, loopflag

cnt, ans = 0, 0
while RCA and cnt < H+W:
    a, r, c = RCA.popleft()
    c += H
    if uf.root(r) == uf.root(c):
        if uf.root(r) == uf.root(H+W):  # loop?
            continue
        uf.unite(r, H+W)
    ans += a
    cnt += 1
    uf.unite(r, c)

print(ans)
