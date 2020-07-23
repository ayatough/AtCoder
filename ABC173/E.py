N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7

A.sort(key=lambda x: abs(x), reverse=True)
best = [1, -1]
k = [0, 0]
for a in A:
    if a == 0:
        break
    elif a > 0:
        if k[0] < K:
            best[0] = (best[0]*a)%MOD
            k[0] += 1
        if k[1] < K:
            if k[1] > 0:
                best[1] = (best[1]*a)%MOD
                k[1] += 1
    else:
        tbest = best.copy()
        tk = k.copy()
        if k[1] < K:
            if k[1] > 0:
                if tbest[0] < tbest[1]*a:
                    best[0] = (tbest[1]*a)%MOD
                    k[0] = tk[1]+1
        if k[0] < K:
            if tbest[1] > tbest[0]*a:
                best[1] = (tbest[0]*a)%MOD
                k[1] = tk[0]+1

if k[0] == K:
    ans = best[0]
else:
    ans = 1
    for k in range(K):
        ans = (ans*A[-1-k])%MOD
print(ans)
