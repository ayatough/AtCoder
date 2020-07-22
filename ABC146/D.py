from collections import deque
N = int(input())
P = [[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    P[a-1].append((b-1, i))
    P[b-1].append((a-1, i))
ans = [0] * N
q = deque()
q.append((0, 0))
colmax = 0
while q:
    u, pcol = q.popleft()
    icol = 1
    for v, i in P[u]:
        if ans[i] != 0:
            continue
        if icol == pcol:
            icol += 1
        ans[i] = icol
        q.append((v, icol))
        colmax = max(colmax, icol)
        icol += 1

print(colmax)
for i in range(N-1):
    print(ans[i])
