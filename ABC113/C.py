N, M = map(int, input().split())
pyi = [[] for _ in range(N)]

for i in range(M):
    p, y = map(int, input().split())
    pyi[p-1].append((y, i))

for i in range(N):
    pyi[i].sort()

O = [None for _ in range(M)]
for p, yis in enumerate(pyi):
    for j, yi in enumerate(yis):
        y, i = yi
        O[i] = (p+1, j+1)

for p, i in O:
    p = ('000000' + str(p))[-6:]
    i = ('000000' + str(i))[-6:]
    print(p+i)
