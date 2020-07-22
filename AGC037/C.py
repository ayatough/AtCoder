from collections import deque
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# check reachability B -> A ?
# 隣接和table
P = [B[(i-1)%N] + B[(i+1)%N] for i in range(N)]
D = deque(i for i in range(N) if B[i] - P[i] >= A[i])
ans = 0
nmatch = [B[i] == A[i] for i in range(N)].count(True)
while D:
    upd = False
    i = D.popleft()
    if B[i] == A[i]:
        nmatch += 1
        continue
    if B[i] <= P[i]:
        continue
    if B[i] - P[i] >= A[i]:
        n = (B[i] - A[i]) // P[i]
        P[(i-1)%N] -= P[i] * n
        P[(i+1)%N] -= P[i] * n
        B[i] -= P[i] * n
        upd = True
        ans += n
        if B[i] == A[i]:
            nmatch += 1
        if B[(i-1)%N] - P[(i-1)%N] >= A[(i-1)%N]:
            D.append((i-1)%N)
        if B[(i+1)%N] - P[(i+1)%N] >= A[(i+1)%N]:
            D.append((i+1)%N)
    if not upd:
        break

print(ans if nmatch == N else -1)
