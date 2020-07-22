# input
N, M = map(int, input().split())
L = []
for _ in range(M):
    L.append(tuple(map(int, input().split())))


def make_vertex_connection(links, vtx_num):
    vc = {i: [] for i in range(1, vtx_num+1)}
    for ab in links:
        a, b = ab
        vc[a].append(b)
        vc[b].append(a)
    return vc


def make_connected(vc, s):
    con = [s]
    q = [s]
    while len(q) > 0:
        u = q.pop()
        for v in vc[u]:
            if v not in con:
                con.append(v)
                q.append(v)
    return con


def make_isolates(vc: dict):
    iso = []
    visit_q = list(vc.keys())
    while len(visit_q) > 0:
        u = visit_q.pop()
        con = make_connected(vc, u)
        iso.append(con)
        for i in con:
            if i == u:
                continue
            visit_q.remove(i)
    return iso


def update_vc_unlink(vc, link):
    a, b = link
    updvc = vc.copy()
    updvc[a].remove(b)
    updvc[b].remove(a)
    return updvc


from itertools import combinations
def get_deghuben(iso):
    if len(iso) == 1:
        iso.append([])
    deg = 0
    for comb in combinations((len(i) for i in iso), 2):
        deg += comb[0] * comb[1]
    return deg


vc = make_vertex_connection(L, N)


for l in L:
    vc = update_vc_unlink(vc, l)
    iso = make_isolates(vc)
    print(get_deghuben(iso))
