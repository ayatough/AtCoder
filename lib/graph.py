'''
二部グラフ　⊃　木
'''


import sys
input = sys.stdin.readline
N = int(input())
V = []
for i in range(N):
    V.append(list(map(int, input())))

INF = float('inf')

# 隣接行列, 無向グラフ, ベルマンフォード
def get_distances(s):
    '''グラフVにおいてsから各ノードへの距離のリストを返却
    '''
    from collections import deque
    q = deque()
    q.append(s)
    d = [INF] * N
    d[s] = 0
    while len(q):
        u = q.popleft()
        for v, e in enumerate(V[u]):
            if e:
                if d[v] > d[u] + 1:
                    d[v] = d[u] + 1
                    q.append(v)
    return d


# 隣接行列, 二部グラフ
def get_diameter():
    dmax = 0
    for i in range(N):
        d = get_distances(i)
        dmax = max(max(d), dmax)
    return dmax


# 隣接行列, 木
def get_diameter():
    '''隣接行列Vによるグラフ直径を返却
    '''
    d = get_distances(0)
    dmax = max(d)
    dindex = d.index(dmax)
    d = get_distances(dindex)
    return max(d)


# 隣接行列, 無向グラフ
def is_bipartite_graph():
    '''二部グラフかどうかを判定
    '''
    from collections import deque
    team = [0] * N
    valid = True
    q = deque()
    q.append(0)
    team[0] = 1
    while valid and len(q):
        u = q.popleft()
        for v, e in enumerate(V[u]):
            if e:
                if not team[v]:
                    team[v] = team[u]%2 + 1
                    q.append(v)
                else:
                    if (team[v] - team[u])%2 == 0:
                        valid = False
                        break
    return valid


# ワーシャル・フロイド
# N頂点のグラフ, VはNxNの二次元配列
# 頂点i-j間の最短距離`V[i][j]`を返す
# 入力のVはINFで初期化されているものとする
# 入力のVにはすでに直接結ばれている2頂点間の距離が入っているものとする
def warshall_floyd(V):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if V[i][j] > V[i][k] + V[k][j]:
                    V[i][j] = V[i][k] + V[k][j]


if __name__ == "__main__":
    pass