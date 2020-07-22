N = int(input())

Q = []
for _ in range(N):
    x, y, h = map(int, input().split())
    Q.append((h, x, y))
Q.sort(reverse=True)

seikai = True
for yc in range(101):
    seikai = False
    for xc in range(101):
        valid = True
        h, x, y = Q[0]
        hc = abs(x-xc) + abs(y-yc) + h
        for (h, x, y) in Q:
            if h == 0:
                if hc > abs(x-xc) + abs(y-yc) + h:
                    valid = False
                    break
            else:
                if hc != abs(x-xc) + abs(y-yc) + h:
                    valid = False
                    break
        if not valid:
            continue
        seikai = True
        break
    if seikai:
        break

print(xc, yc, hc)
