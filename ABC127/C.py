N, M = map(int, input().split())

L, R = [], []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

dif = min(R) - max(L)
print(dif + 1 if dif >= 0 else 0)
