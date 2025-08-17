from collections import deque

N, K = map(int, input().split())
X = [-1]
X.extend(list(map(int, input().split())))
A = [-1]
A.extend(list(map(int, input().split())))

CON = []  # connected component id which is loop node
ICON = [-1] * (N+1)  # connected component table
VIS = [False] * (N+1)  # visited flag
D = [-1] * (N+1)  # distance to loop node

icnt = 0
for i in range(1, N+1):
    if VIS[i]:
        continue
    Q = deque([i])
    while not VIS[Q[-1]]:
        VIS[Q[-1]] = True
        x = X[Q[-1]]
        Q.append(x)
        if ICON[x] >= 0:
            break
    Q.pop()
    if ICON[x] < 0:
        d = 0
        CON.append(Q[-1])
        while Q:
            q = Q.pop()
            D[q] = d
            d += 1
            ICON[q] = icnt
        icnt += 1
    else:
        d = D[x] + 1
        while Q:
            q = Q.pop()
            D[q] = d
            d += 1
            ICON[q] = ICON[x]

print(D)
print(CON)
print(ICON)

ans = [-1] * (N+1)

for i in range(1, N+1):
    icon = ICON[i]
    loop_node = CON[icon]
    loop_len = X[loop_node] + 1
    d = D[i]
    k = K
    j = i
    if d <= k:
        j = loop_node
        k = (k - d) % loop_len
    while k > 0:
        j = X[j]
        k -= 1
    ans[i] = A[j]

print(*ans[1:])
