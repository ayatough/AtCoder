M, N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(1,M+1):
    tbl = [False for _ in range(K)]
    tmp = 0
    for x in X:
        v = abs(x-i)
        if v == 0:
            tmp += 1
        elif v <= K:
            tbl[v-1] |= True
    tmp += tbl.count(True)
    ans = max(ans, tmp)

print(ans)
