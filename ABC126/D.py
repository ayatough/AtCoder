N = int(input())
U, V, W = [], [], []
T = [[] for _ in range(N)]
# tree
class Tree(object):
    def __init__(self, us, vs, ws):
        self.con_table = [[] for _ in range(len(us) + 1)]
        self.weights = dict()
        for (u, v, w) in zip(us, vs, ws):
            self.con_table[u-1].append(v-1)
            self.con_table[v-1].append(u-1)
            self.weights[(u-1, v-1)] = w


dists = [None for _ in range(N)]


def initiate():
    dists[0] = 0

def core(u, v, tree):
    dists[u] = dists[v] + tree.weights[(min(u, v), max(u, v))]

def dfs(tree, initiate, core):
    from collections import deque
    initiate()
    visited = [False for _ in range(len(tree.con_table))]
    while not all(visited):
        search = deque()
        visited[0] = True
        search.append(0)
        while len(search) > 0:
            v = search.pop()
            for u in tree.con_table[v]:
                if not visited[u]:
                    core(u, v, tree)
                    visited[u] = True
                    search.append(u)
# S = set()
for _ in range(N-1):
    u, v, w = map(int, input().split())
    # if w % 2 == 1:
    #     T[u-1].append(v)
    #     T[v-1].append(u)
    #     S.add(u)
    #     S.add(v)
    U.append(u)
    V.append(v)
    W.append(w)

tree = Tree(U, V, W)

dfs(tree, initiate, core)

# ans = [None for _ in range(N)]

# while len(S) > 0:
#     s = S.pop()
#     search = set()
#     search.add(s)
#     ans[s-1] = '0'
#     while len(search) > 0:
#         p = search.pop()
#         if p in S:
#             S.remove(p)
#         for t in T[p-1]:
#             if t in S:
#                 search.add(t)
#                 ans[t-1] = '0' if ans[p-1] == '1' else '1'

# for i in range(N):
#     if ans[i] is None:
#         ans[i] = '0'
    

# print(' '.join(ans))

print('\n'.join(('0' if d % 2 == 0 else '1') for d in dists))
