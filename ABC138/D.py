import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, Q = map(int, input().split())
V = {i: [] for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

C = {i: 0 for i in range(1,N+1)}

for _ in range(Q):
    p, x = map(int, input().split())
    C[p] += x


def propagate(u, p):
    for v in V[u]:
        if v == p:
            continue
        C[v] += C[u]
        propagate(v, u)

propagate(1, 0)

# print(' '.join(str(C[i]) for i in range(1,N+1)))
print(*C.values())
