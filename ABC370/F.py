from itertools import combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)
A = A + A

lo = 1
hi = sumA // K + 1

INF = 2*10**13

def divisible(minw):
    digit = len(bin(K)[2:])
    DB = [[INF] * N for _ in range(digit)]
    F = DB[0]  # next index of cut
    cum = 0
    head, tail = 0, 0
    while tail < N and head < N*2:
        if cum < minw:
            # forward head
            cum += A[head]
            head += 1
            if cum >= minw:
                F[tail] = head
                cum -= A[tail]
                tail += 1
        else:
            # backward head
            if cum - A[head-1] < minw:
                F[tail] = head
                cum -= A[tail]
                tail += 1
            else:
                head -= 1
                cum -= A[head]

    # calc table
    for k in range(1,digit):
        for i in range(N):
            if DB[k-1][i] < N:
                DB[k][i] = DB[k-1][DB[k-1][i]]
            elif DB[k-1][i] < INF:
                DB[k][i] = DB[k-1][DB[k-1][i] - N] + N
                if DB[k][i] >= 2*N:
                    DB[k][i] = INF
            else:
                DB[k][i] = INF

    # print(f"{DB=}")

    num_ok = 0
    for i in range(N):
        ok = True
        s = i
        for k in range(digit-1,-1,-1):
            if (1 << k) & K:
                if s < N:
                    s = DB[k][s]
                else:
                    s = DB[k][s - N] + N

                if s == INF or s > i + N:
                    ok = False
                    break
        if ok:
            num_ok += 1
    return num_ok


ans = N
while lo + 1 < hi:
    mi = (lo + hi) >> 1
    # print(f"{lo=}, {hi=}, {mi=}")
    num_ok = divisible(mi)
    if num_ok > 0:
        ans = num_ok
        lo = mi
    else:
        hi = mi

print(lo, N - ans)
