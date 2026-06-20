Q = int(input())

c = {}

for _ in range(Q):
    q = input().strip().split()
    if len(q) == 2:
        q, x = map(int, q)
        if q == 1:
            if x in c:
                c[x] += 1
            else:
                c[x] = 1
        else:
            c[x] -= 1
            if c[x] == 0:
                del c[x]
    else:
        print(len(c))
