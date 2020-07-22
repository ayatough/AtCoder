N, X = map(int, input().split())
tbl = []
trg = 0
for _ in range(N):
    b, l, u = map(int, input().split())
    ary, arysum = [l] * b + [u] * (X-b), l*b + u*(X-b)
    tbl.append((arysum, ary))
    trg += l*b

tbl.sort(reverse=True)

lo, hi = 0, X*N

def judge(lo, hi):
    if lo == hi:
        return lo
    k = (lo + hi)//2
    q, r = divmod(k, X)
    bas = sum(tbl[i][0] for i in range(q+1))
    ma = 0
    for i in range(N):
        m = bas + sum(tbl[i][1][j] for j in range(r)) - tbl[min(i,q)][0]
        if m > ma:
            ma = m
    if ma >= trg:
        return judge(lo, k)
    else:
        return judge(k+1, hi)

print(judge(lo, hi))
