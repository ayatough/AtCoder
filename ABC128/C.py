from itertools import product

N, M = map(int, input().split())
KS = []
for _ in range(M):
    kss = list(map(int, input().split()))
    KS.append(kss)

P = list(map(int, input().split()))

count = 0
for sw in product((0, 1), repeat=N):
    judge = True
    for i in range(M):
        on = 0
        for s in KS[i][1:]:
            on += sw[s-1]
        if on % 2 != P[i]:
            judge = False
            break
    if judge:
        count += 1

print(count)
