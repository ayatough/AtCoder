from collections import deque

V, E = map(int, input().split())

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
for _ in range(E):
    u, v, c = map(int, input().split())
    graph.add_flow(u, v, c)

print(graph.solve(0, V-1))
