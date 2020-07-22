# input
n = int(input())

# 1. make validate graph fragment (all index are includede completely)
fragments = []
if n % 2 == 0:
    # even case: (1, n), (2, n-1), ..., (n//2, n//2+1)
    fragments = [(i + 1, n - i) for i in range(n // 2)]
else:
    # odd case: (1, n-1), (2, n-2), ..., (n//2-1, n//2+1), (n)
    fragments = [(i + 1, n - i - 1) for i in range(n // 2)]
    fragments.append((n,))

# 2. each vertex connect all vertex excepy for one's belonging graph's element
edges = []
for i, frag in enumerate(fragments):
    for vtx in frag:
        other_frags = fragments[:i] + fragments[i + 1:]
        edges.extend([(vtx, o_vtx) for o_frag in other_frags for o_vtx in o_frag])

# 3. delete duplicated edge (remain (a, b) edge for a < b)
for edge in edges[:]:
    if edge[0] > edge[1]:
        edges.remove(edge)


print(len(edges))
for edge in edges:
    print(' '.join(str(i) for i in edge))
