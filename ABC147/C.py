from itertools import product
N = int(input())
A = [[] for _ in range(N)]
for i in range(N):
    na = int(input())
    for j in range(na):
        x, y = map(int, input().split())
        A[i].append((x-1, y))
ans = 0
for pat in product((0, 1), repeat=N):
    num = pat.count(1)
    mujun = False
    for i, shogen in enumerate(A):
        if pat[i] == 0:
            continue
        for s in shogen:
            x, y = s
            if pat[x] != y ^ (1 - pat[i]):
                mujun = True
                break
        if mujun:
            break
    if mujun:
        continue
    ans = max(ans, num)
print(ans)
