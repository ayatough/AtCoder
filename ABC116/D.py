from heapq import heappop, heappush
N, K = map(int, input().split())
KMAX = 10 ** 5 + 1
TD = []
for _ in range(N):
    t, d = map(int, input().split())
    TD.append((d, t))

TD.sort(reverse=True)

pioneer = []
successor = []
appear = [False] * KMAX
cnt = 0
nsp = 0  # num of species
base = 0
best = []

for td in TD:
    d, t = td
    if cnt < K:
        heappush(successor if appear[t] else pioneer, (d, t))
        nsp += 0 if appear[t] else 1
        appear[t] = True
        base += d
        cnt += 1
        if cnt == K:
            heappush(best, -(base + nsp ** 2))
        continue
    if not successor:
        break
    if appear[t]:
        continue
    cd, ct = heappop(successor)
    appear[t] = True
    heappush(pioneer, (d, t))
    base += (d-cd)
    nsp += 1
    heappush(best, -(base + nsp ** 2))

print(-heappop(best))
