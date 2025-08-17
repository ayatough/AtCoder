from heapq import heapify, heappop, heappush
T = int(input())
INF = 10**13

def solve(N, K, A):
    D = [INF] * N
    V = [False] * N
    H = [(0, 0)]
    heapify(H)
    D[0] = 0
    while H:
        d, u = heappop(H)
        V[u] = True
        for v in A[u]:
            if V[v]:
                continue
            D[v] = min(D[v], d + 1)
            heappush(H, (D[v], v))

    cnt = []
    for i in range(1, N):
        if D[i] >= K and D[i] % K == 0:
            cnt.append(D[i] // K)
        else:
            cnt.append(-1)

    return cnt


ans = []
for _ in range(T):
    N, K = map(int, input().split())
    A = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        A[u-1].append(v-1)
        A[v-1].append(u-1)
    ans.append(solve(N, K, A))

for a in ans:
    print(*a)
