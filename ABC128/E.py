from bisect import insort_left

N, Q = map(int, input().split())
XST, D = [], []
# D = []
DMAX = 10 ** 9
# STOP = [DMAX for _ in range(10 ** 9)]
for _ in range(N):
    s, t, x = map(int, input().split())
    # a, b = max(0, s-x), min(10 ** 9, t-x)
    # for i in range(a, b):
        # STOP[i] = min(x, STOP[i])
    insort_left(XST, (x, s, t))
    # XST.append((x, s, t))

for _ in range(Q):
    D.append(int(input()))

# XST.sort()

def stop(x, s, t, d):
    arv = d + x
    if s <= arv < t:
        return 1
    elif arv >= t:
        return 2
    return 0

    

# def stoppable(x, s, t):


for d in D:
    go = -1
    for xst in XST[:]:
        res = stop(xst[0], xst[1], xst[2], d)
        if res == 1:
            go = xst[0]
            break
        elif res == 2:
            XST.remove(xst)
    print(go)
