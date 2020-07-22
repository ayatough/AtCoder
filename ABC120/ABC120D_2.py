# input
N, M = map(int, input().split())
L = []
for _ in range(M):
    L.append(tuple(map(int, input().split())))


def d_conven(islands, bridge):
    a, b = bridge
    a_isl = islands[a]
    b_isl = islands[b]
    d = len(a_isl) * len(b_isl) if b not in a_isl else 0
    islands[a].extend(b_isl)
    for bi in b_isl:
        islands[bi] = islands[a]
    return d

# search from isolated state to initial state
# isolated state
incv = sum(i for i in range(N))
islands = {i: [i] for i in range(1,N+1)}
history = [incv]
for brig in L[::-1]:
    incv -= d_conven(islands, brig)
    history.insert(0, incv)

print('\n'.join(map(str, history[1:])))
