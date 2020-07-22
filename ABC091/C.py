N = int(input())

rs, bs = [], []  # (x, y, pair_flag)

for _ in range(N):
    rs.append(list(map(int, input().split())) + [0])

for _ in range(N):
    bs.append(list(map(int, input().split())) + [0])

rs.sort(key=lambda x: x[1])
bs.sort()

npair = 0
ir, ib = 0, 0
while ib < N:
    bx, by, _ = bs[ib]
    ir = N-1
    while ir >= 0:
        rx, ry, paired = rs[ir]
        if not paired and rx < bx and ry < by:
            rs[ir][2] = bs[ib][2] = 1
            npair += 1
            break
        ir -= 1
    ib += 1

print(npair)
