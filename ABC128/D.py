N, K = map(int, input().split())
V = list(map(int, input().split()))

rich = 0
# bring k jewels
for k in range(1, min(K+1, N+1)):
    for rot in range(k+1):
        jewels = (V[-rot:] + V[:-rot])[:k]
        jewels.sort()
        neg = [i < 0 for i in jewels].count(True)
        # return r jewels
        for ret in range(min(neg+1,K-k+1)):
            rich = max(sum(jewels[ret:]), rich)

print(rich)
