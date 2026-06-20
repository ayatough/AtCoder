N, Q = map(int, input().split())

mas = [0] * N
counter = [0] * (Q + 1)
counter[0] = N
accum = [0] * (Q + 1)
accum[0] = N
minv = 0

for _ in range(Q):
    com, x = map(int, input().split())
    if com == 1:
        counter[mas[x-1]] -= 1
        if mas[x-1] == minv and counter[minv] == 0:
            minv += 1
        mas[x-1] += 1
        counter[mas[x-1]] += 1
        accum[mas[x-1]] += 1
    else:
        # print(counter, accum, minv)
        print(accum[min(x + minv, Q)])
