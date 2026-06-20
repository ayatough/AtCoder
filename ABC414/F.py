from heapq import heapify, heappop, heappush
T = int(input())
INF = 10**13

def solve(N, K, A):
    dp = {}
    for u, a in enumerate(A):
        for v in a:
            dp[(u, v)] = [INF] * (K+1)

    for v in A[0]:
        dp[(0, v)][1] = 1

    q = [0]
    visited = [False] * N
    heapify(q)
    while q:
        v = heappop(q)
        visited[v] = True
        for w in A[v]:
            if visited[w]:
                continue

            for u in range(N):
                if u == v or u == w:
                    continue
                for k in range(1, K):
                    dp[(v, w)][k+1] = min(dp[(v, w)][k+1], dp[(u, v)][k] + 1)

                dp[(v, w)][1] = min(dp[(v, w)][1], dp[(u, v)][K] + 1)

            heappush(q, w)

    print(dp)
    return []

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
