from collections import deque
N, K = map(int, input().split())
A = list(map(int, input().split()))
next_step = [0] * N
memo = [-1] * (2*10**5)
cnt = 0
for i, a in enumerate(A+A):
    if memo[a-1] >= 0:
        if next_step[memo[a-1]%N]:
            continue
        next_step[memo[a-1]%N] = i - memo[a-1] + 1
        if next_step[memo[a-1]%N] == 0:
            pass
        cnt += 1
    if cnt == N:
        break
    memo[a-1] = i

j = 0
while True:
    if j + next_step[j%N] < N*K:
        j += next_step[j%N]
        if j%N == 0:
            j = max(j, N*K//j*j)
    else:
        break

q = deque()
memo = [-1] * (2*10**5)
cnt = 0
for k in range(j, N*K):
    a = A[k%N]
    if memo[a-1] < 0:
        q.append(a)
        memo[a-1] = cnt
        cnt += 1
    else:
        while True:
            b = q.pop()
            memo[b-1] = -1
            if b == a:
                break

print(*q)
