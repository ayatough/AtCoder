from collections import deque
from heapq import heappop, heappush

V, E, F = map(int, input().split())

class DirectedGraph(object):
    def __init__(self, V):
        self._flc = dict()  # {(u0, v0): [f(u0, v0), d(u0, v0)], ...}
        self._lnk = dict()  # {u0 : [v0, v1, v2, ...], u1: [v1, v3, ...], ...}
        self._V = V
        self._h = [0 for _ in range(V)]

    def add_link(self, u, v, c=1):
        if self._lnk.get(u) is None:
            self._lnk[u] = [v]
        else:
            self._lnk[u].append(v)

    def add_flow_cost(self, u, v, c=1, d=1):
        self._flc[(u, v)] = [c, d]
        self._flc[(v, u)] = [0, -d]  # residual flow
        self.add_link(u, v)
        self.add_link(v, u)
    
    def solve(self, s, t):
        path = self._detect_path(s, t)
        max_flow = 0
        min_flow_d = 0
        while path is not None and max_flow < F:
            flow = self._calc_max_path_flow(path)
            # check flow
            if max_flow + flow > F:
                flow = F - max_flow
            max_flow += flow
            min_flow_d += self._get_update_flow_d(path, flow)
            self._reflow_cost(path, flow)
            path = self._detect_path(s, t)
        if max_flow < F:
            return -1
        return min_flow_d

    def _get_update_flow_d(self, path, flow):
        flow_d = 0
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            flow_d += flow * self._flc[(u, v)][1]
        return flow_d

    def _reflow_cost(self, path, cost):
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            self._flc[(u, v)][0] -= cost
            self._flc[(v, u)][0] += cost

    def _calc_max_path_flow(self, path):
        return min(self._flc[(path[i], path[i+1])][0] for i in range(len(path)-1))

    def _detect_path(self, s, t):
        ''' dijkstra '''
        INF = 10 ** 9
        vstd = [False for _ in range(self._V)]
        dist = [INF for _ in range(self._V)]  # distance
        prev = [None for _ in range(self._V)]  # for extract min cost path
        pq = []
        # initialize
        dist[s] = 0
        heappush(pq, (0, s))
        while pq:
            _, u = heappop(pq)
            vstd[u] = True
            for v in self._lnk[u]:
                if vstd[v] or self._flc[(u, v)][0] <= 0:
                    continue
                if dist[u] + self._flc[(u, v)][1] + self._h[u] < dist[v] + self._h[v]:
                    dist[v] = dist[u] + self._flc[(u, v)][1] + self._h[u] - self._h[v]
                    prev[v] = u
                    heappush(pq, (dist[v], v))
        # no path found        
        if prev[t] is None:
            return None
        # update h
        for i in range(self._V):
            self._h[i] += dist[i]
        # extarct min cost path
        path = deque([t])
        while path[0] != s:
            path.appendleft(prev[path[0]])
        
        return path

graph = DirectedGraph(V)
for _ in range(E):
    u, v, c, d = map(int, input().split())
    graph.add_flow_cost(u, v, c, d)

print(graph.solve(0, V-1))
