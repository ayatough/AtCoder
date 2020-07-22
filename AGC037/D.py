# import numpy as np
N, M = map(int, input().split())
V = [[0] * (2*N) for _ in range(2*N)]
E = dict()

class DirectedGraph(object):
    def __init__(self):
        self._flw = dict()  # {(u0, v0): f(u0, v0), (u1, v1): f(u1, v1), ...}
        self._lnk = dict()  # {u0 : [v0, v1, v2, ...], u1: [v1, v3, ...], ...}

    def add_link(self, u, v, c=1):
        if self._lnk.get(u) is None:
            self._lnk[u] = [v]
        else:
            self._lnk[u].append(v)

    def add_flow(self, u, v, c=1):
        self._flw[(u, v)] = c
        self._flw[(v, u)] = 0  # residual flow
        self.add_link(u, v)
        self.add_link(v, u)
    
    def solve(self, s, t):
        path = self._detect_path(s, t)
        max_flow = 0
        while path is not None:
            cost = self._calc_max_path_flow(path)
            max_flow += cost
            self._reflow_cost(path, cost)
            path = self._detect_path(s, t)
        return max_flow

    def _reflow_cost(self, path, cost):
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            self._flw[(u, v)] -= cost
            self._flw[(v, u)] += cost

    def _calc_max_path_flow(self, path):
        return min(self._flw[(path[i], path[i+1])] for i in range(len(path)-1))

    def _detect_path(self, s, t):
        ''' dfs '''
        visited = [0 for _ in range(V)]
        def dfs(u, path):
            if u == t:
                return path
            if visited[u]:
                return
            visited[u] = 1
            for v in self._lnk[u]:
                if v in path or self._flw[(u, v)] <= 0:
                    continue
                l = dfs(v, path + [v])
                if l is not None:
                    return l
        p = dfs(s, [s])
        return p

graph = DirectedGraph()

for i in range(N):
    for a in list(map(int, input().split())):
        m = (a-1)//M + N
        # V[i][m] += 1
        # V[m][i] += 1
        graph.add_flow(i, m)
        if (i, m) in E:
            E[(i, m)] += [a]
        else:
            E[(i, m)] = [a]

graph.add_flow()

# def search():
#     match = [0] * N
#     reserved = [False] * N
#     i = 0
#     nmatch = 0
#     # search
#     while nmatch < N:
#         if i < N:
#             if match[i]:
#                 i += 1
#                 i %= N
#                 continue
#             for j in range(N,2*N):
#                 if reserved[j%N]:
#                     continue
#                 if V[i][j] > 0:
#                     V[i][j] -= 1
#                     V[j][i] -= 1
#                     match[i] = E[(i, j)].pop()
#                     reserved[j%N] = True
#                     nmatch += 1
#                     i = j
#                     break
#         else:
#             for j in range(N):
#                 if match[j]:
#                     continue
#                 if V[j][i] > 0:
#                     i = j
#                     break
#             else:
#                 i = 0
#     return match

# CR = np.array([search() for _ in range(M)])
CR = [search() for _ in range(M)]

# 1st
# for r in range(N):
#     print(*CR[:,r])
for r in range(N):
    print(*[CR[c][r] for c in range(M)])

# 2nd
# CR.sort()
for c in range(M):
    CR[c].sort()
# for r in range(N):
#     print(*CR[:,r])
for r in range(N):
    print(*[CR[c][r] for c in range(M)])
